#!/usr/bin/python
from __future__ import print_function
import json
import sys
from urllib2 import HTTPError, urlopen
import ssl
import time
import datetime

TIMEOUT = 10
BASE_URL = "https://blockchain.info/"

class Input:
    def __init__(self, i):
        obj = i.get('prev_out')
        if obj is not None:
            self.flag = True
            self.n = obj['n']
            self.value = obj['value']
            if 'addr' in obj:
                self.address = obj['addr']
            else:
                self.address = 'none'
            self.tx_index = obj['tx_index']
            self.type = obj['type']
            self.script = obj['script']
            self.script_sig = i['script']
            self.sequence = i['sequence']
        else:
            self.flag = False
            self.script_sig = i['script']
            self.sequence = i['sequence']

class Output:
    def __init__(self, o):
        self.n = o['n']
        self.value = o['value']
        self.address = o.get('addr')
        self.tx_index = o['tx_index']
        self.script = o['script']
        self.spent = o['spent']


class Transaction:
    def __init__(self, t):
        self.double_spend = t.get('double_spend', False)
        self.block_height = t.get('block_height')
        self.time = t['time']
        self.relayed_by = t['relayed_by']
        self.hash = t['hash']
        self.tx_index = t['tx_index']
        self.version = t['ver']
        self.size = t['size']
        self.inputs = [Input(i) for i in t['inputs']]
        self.outputs = [Output(o) for o in t['out']]

        if self.block_height is None:
            self.block_height = -1

class Block:
    def __init__(self, b):
        self.hash = b['hash']
        self.version = b['ver']
        self.previous_block = b['prev_block']
        self.merkle_root = b['mrkl_root']
        self.time = b['time']
        self.bits = b['bits']
        self.fee = b['fee']
        self.nonce = b['nonce']
        self.n_tx = b['n_tx']
        self.size = b['size']
        self.block_index = b['block_index']
        self.main_chain = b['main_chain']
        self.height = b['height']
        self.received_time = b.get('received_time', b['time'])
        self.relayed_by = b.get('relayed_by')
        self.transactions = [Transaction(t) for t in b['tx']]
        for tx in self.transactions:
            tx.block_height = self.height

class APIException(Exception):
    def __init__(self, message, code):
        Exception.__init__(self, message)
        self.code = code

APIKey = "66b03cf5-2c55-4aef-bf2c-8e6d0f3b31dc"

def get_tx(tx_id):
    resource = 'rawtx/' + tx_id + '?api_code=' + APIKey
    response = call_api(resource)
    json_response = json.loads(response)
    return Transaction(json_response)

def handle_response(response):
    if isinstance(response, str):
        return response
    else:
        return response.decode('utf-8')

def call_api(resource, data=None, base_url=None):
    base_url = BASE_URL if base_url is None else base_url
    try:
        payload = None if data is None else urlencode(data)
        response = urlopen(base_url + resource, payload, timeout=TIMEOUT).read()
        return handle_response(response)
            
    except HTTPError as e:
        raise APIException(handle_response(e.read()), e.code)

def get_block(block_id):
    resource = 'rawblock/' + block_id + '?api_code=' + APIKey
    response = call_api(resource)
    json_response = json.loads(response)
    return Block(json_response)

def get_blocks(time):
    resource = 'blocks/{0}?format=json' + '&api_code=' + APIKey
    resource = resource.format(time)
    response = call_api(resource)
    json_response = json.loads(response)
    return [SimpleBlock(b) for b in json_response['blocks']]

class SimpleBlock:
    def __init__(self, b):
        self.hash = b['hash']
        self.main_chain = b['main_chain']


import networkx as nx


g = nx.DiGraph()
timestamp = int(time.time())
size = 0
d = {}
blocks = get_blocks(time = (timestamp * 1000))
num = 0
for i in range(7):
    for block in blocks:
        try:
            if block.main_chain == False:
                continue
            block_info = get_block(block.hash)
            for tx in block_info.transactions:
                for i in tx.inputs:
                    if i.flag == False:
                        continue
                    for o in tx.outputs:
                        w = float(o.value)
                        if (g.has_edge(i.address, o.address)):
                            w += g[i.address][o.address]['weight']
                            g.remove_edge(i.address, o.address)
                        g.add_edge(i.address, o.address, weight = w)
        except ssl.SSLError:
            continue
        except APIException:
            print('error')
    timestamp -= 86411
nx.write_gexf(g, 'graph.gexf')