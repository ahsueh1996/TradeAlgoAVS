"""
Goto the website and paste the curl command below to convert to python requests
**********************************************************************************************************************************
***** Remember to protect your privacy and remove any sensitive information before pasting the curl command to the website *******
************************************************ https://curlconverter.com/ ******************************************************

curl 'https://my.wealthsimple.com/graphql' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'authorization: Bearer eyJhbGcMTczNTkzNDAxNiwi....yhvXeS8AZqvbx-YGwfXIWHjiyL7OzPuwBdceZVVQXePEt...HIabYYiZ42ZFtyrC4qwPn6OTbZV7jMXpI0nEp...Mpwap9WaTsR3YvuoVs0c3jonszsAUayRuUYyjpBCL3HDDOZCRX9-lLZ88T4qYdfzzdGui7dvG2dyibbFSGCXAKzl8nWmEh2BNJo_YMubI62Ajfog' \
  -H 'content-type: application/json' \
  -H 'cookie: ws_global_visitor_id=5f51a681-3c43-4db9-9342-ed24798724c0; _session_id=84a4778702c147021fa8c0973734a285; _tt_enable_cookie=1; IR_gbd=wealthsimple.com; wssdi=41521b683939e86c668e7b34745c8461; ajs_user_id=user-r2bl3nnqhso; _ttp=ENEQvi1xSYojKm8TnqLykO1CCs0.tt.1; _cfuvid=N2itggAkvLojQXcSHSMq.6czzTsnSIBcgN4xDefRWRw-1735929829001-0.0.1.1-604800000; ws_global_visitor_id=2f6df067-a378-44d7-a510-d0a63bf4a3c9; ajs_anonymous_id=aea41d51-0363-4b63-84e9-8157535b9335; _oauth2_access_v2=%7B%22access_token%22%3A%22eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJpZGVudGl0eS1tbEoydE5DdmtHM0IzTzM2emk2MnNMME9ET1UiLCJleHAiOjE3MzU5MzU4MTYsImlhdCI6MTczNTkzNDAxNiwianRpIjoiX1BfWnVNcHpNTG9OdlpLVDNqUkE5WC1Fd0EwVmVXRjRja3FKejltYU8tYyIsImNsaWVudF9pZCI6IjRkYTUzYWMyYjAzMjI1YmVkMTU1MGViYThlNDYxMWUwODZjN2I5MDVhMzg1NWU2ZWQxMmVhMDhjMjQ2NzU4ZmEiLCJzY29wZSI6ImludmVzdC5yZWFkIGludmVzdC53cml0ZSB0cmFkZS5yZWFkIHRyYWRlLndyaXRlIHRheC5yZWFkIHRheC53cml0ZSJ9.0j73lzNrJVRSjhMp6a1yq3ifzBXaqTc_1cHS1oCZAo5YyuyhvXeS8AZqvbx-YGwfXIWHjiyL7OzPuwBdceZVVQXePEtA1axkyA533OEu32wFClqvoYzBJ_SkQqLlBQiIz_lRjnDd1ncECuDJo6S75l2_4YaogHIabYYiZ42ZFtyrC4qwPn6OTbZV7jMXpI0nEpqGMT_hAV4def8qaDLCgJEIT2b0lRJptXCCQqMpwap9WaTsR3YvuoVs0c3jonszsAUayRuUYyjpBCL3HDDOZCRX9-lLZ88T4qYdfzzdGui7dvG2dyibbFSGCXAKzl8nWmEh2BNJo_YMubI62Ajfog%22%2C%22token_type%22%3A%22Bearer%22%2C%22expires_in%22%3A1800%2C%22refresh_token%22%3A%22EIcyM8ai-uNNPrj2bSojr_y6FrWcpAcUbC8t8G87PoM%22%2C%22scope%22%3A%22invest.read%20invest.write%20trade.read%20trade.write%20tax.read%20tax.write%22%2C%22created_at%22%3A1735934016%2C%22okta_group_claims%22%3A%5B%5D%2C%22identity_canonical_id%22%3A%22identity-mlJ2tNCvkG3B3O36zi62sL0ODOU%22%2C%22clock_skew%22%3A%7B%22skewed%22%3Afalse%7D%2C%22expires_at%22%3A%222025-01-03T20%3A23%3A36.000Z%22%2C%22email%22%3A%22ahsueh1996%40gmail.com%22%2C%22profiles%22%3A%7B%22tax%22%3A%7B%22default%22%3A%22user-eedww24xbft%22%7D%2C%22trade%22%3A%7B%22default%22%3A%22user-ejs4xw9bbkg%22%7D%2C%22invest%22%3A%7B%22default%22%3A%22user-r2bl3nnqhso%22%7D%7D%2C%22client_canonical_ids%22%3A%7B%22tax%22%3A%7B%22default%22%3A%22person-bdiuyqifzp6yeg%22%7D%2C%22trade%22%3A%7B%22default%22%3A%22person-dnvo5jjaio1pfq%22%7D%2C%22invest%22%3A%7B%22default%22%3A%22person-1p_oiha5naqupq%22%7D%7D%2C%22suspended_profiles%22%3A%7B%7D%7D; IR_5571=1735934383548%7C0%7C1735934383548%7C%7C; ab.storage.deviceId.80ec85f3-36f6-4cc8-8401-81fb1619363d=g%3A26157de1-4856-dbfa-e484-f715e455a091%7Ce%3Aundefined%7Cc%3A1734911250207%7Cl%3A1735934384547; ab.storage.userId.80ec85f3-36f6-4cc8-8401-81fb1619363d=g%3Aidentity-mlJ2tNCvkG3B3O36zi62sL0ODOU%7Ce%3Aundefined%7Cc%3A1734911250205%7Cl%3A1735934384547; ab.storage.sessionId.80ec85f3-36f6-4cc8-8401-81fb1619363d=g%3Af4bc6009-82e0-4757-e023-792c50e07664%7Ce%3A1735934684560%7Cc%3A1735934384547%7Cl%3A1735934384560; _dd_s=rum=0&expire=1735935690298' \
  -H 'origin: https://my.wealthsimple.com' \
  -H 'priority: u=1, i' \
  -H 'referer: https://my.wealthsimple.com/app/security-details/sec-s-86f44a72211b4effaf2bd1bafddadf1e?account=non-registered-OIzSXMKX6w' \
  -H 'sec-ch-ua: "Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' \
  -H 'x-platform-os: web' \
  -H 'x-ws-api-version: 12' \
  -H 'x-ws-device-id: 41521b683939e86c668e7b34745c8461' \
  -H 'x-ws-locale: en-CA' \
  -H 'x-ws-profile: trade' \
  --data-raw $'{"operationName":"SoOrdersOrderCreate","variables":{"input":{"canonicalAccountId":"non-registered-OIzSXMKX6w","externalId":"order-189b089d-68e9-4064-97f8-b8ddfe288fd4","executionType":"LIMIT","orderType":"BUY_QUANTITY","quantity":1,"securityId":"sec-s-86f44a72211b4effaf2bd1bafddadf1e","timeInForce":"DAY","limitPrice":8,"extendedHoursOrder":false}},"query":"mutation SoOrdersOrderCreate($input: SoOrders_CreateOrderInput\u0021) {\\n  soOrdersCreateOrder(input: $input) {\\n    errors {\\n      code\\n      message\\n      __typename\\n    }\\n    order {\\n      orderId\\n      createdAt\\n      __typename\\n    }\\n    __typename\\n  }\\n}"}'

"""

# paste the python code below
import requests

cookies = {
    'ws_global_visitor_id': '5f51a681-3c43-4db9-9342-ed24798724c0',
    '_session_id': '84a4778702c147021fa8c0973734a285',
    '_tt_enable_cookie': '1',
    'IR_gbd': 'wealthsimple.com',
    'wssdi': '41521b683939e86c668e7b34745c8461',
    'ajs_user_id': 'user-r2bl3nnqhso',
    '_ttp': 'ENEQvi1xSYojKm8TnqLykO1CCs0.tt.1',
    '_cfuvid': 'N2itggAkvLojQXcSHSMq.6czzTsnSIBcgN4xDefRWRw-1735929829001-0.0.1.1-604800000',
    'ws_global_visitor_id': '2f6df067-a378-44d7-a510-d0a63bf4a3c9',
    'ajs_anonymous_id': 'aea41d51-0363-4b63-84e9-8157535b9335',
    '_oauth2_access_v2': '%7B%22access_token%22%3A%22eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJpZGVudGl0eS1tbEoydE5DdmtHM0IzTzM2emk2MnNMME9ET1UiLCJleHAiOjE3MzU5MzU4MTYsImlhdCI6MTczNTkzNDAxNiwianRpIjoiX1BfWnVNcHpNTG9OdlpLVDNqUkE5WC1Fd0EwVmVXRjRja3FKejltYU8tYyIsImNsaWVudF9pZCI6IjRkYTUzYWMyYjAzMjI1YmVkMTU1MGViYThlNDYxMWUwODZjN2I5MDVhMzg1NWU2ZWQxMmVhMDhjMjQ2NzU4ZmEiLCJzY29wZSI6ImludmVzdC5yZWFkIGludmVzdC53cml0ZSB0cmFkZS5yZWFkIHRyYWRlLndyaXRlIHRheC5yZWFkIHRheC53cml0ZSJ9.0j73lzNrJVRSjhMp6a1yq3ifzBXaqTc_1cHS1oCZAo5YyuyhvXeS8AZqvbx-YGwfXIWHjiyL7OzPuwBdceZVVQXePEtA1axkyA533OEu32wFClqvoYzBJ_SkQqLlBQiIz_lRjnDd1ncECuDJo6S75l2_4YaogHIabYYiZ42ZFtyrC4qwPn6OTbZV7jMXpI0nEpqGMT_hAV4def8qaDLCgJEIT2b0lRJptXCCQqMpwap9WaTsR3YvuoVs0c3jonszsAUayRuUYyjpBCL3HDDOZCRX9-lLZ88T4qYdfzzdGui7dvG2dyibbFSGCXAKzl8nWmEh2BNJo_YMubI62Ajfog%22%2C%22token_type%22%3A%22Bearer%22%2C%22expires_in%22%3A1800%2C%22refresh_token%22%3A%22EIcyM8ai-uNNPrj2bSojr_y6FrWcpAcUbC8t8G87PoM%22%2C%22scope%22%3A%22invest.read%20invest.write%20trade.read%20trade.write%20tax.read%20tax.write%22%2C%22created_at%22%3A1735934016%2C%22okta_group_claims%22%3A%5B%5D%2C%22identity_canonical_id%22%3A%22identity-mlJ2tNCvkG3B3O36zi62sL0ODOU%22%2C%22clock_skew%22%3A%7B%22skewed%22%3Afalse%7D%2C%22expires_at%22%3A%222025-01-03T20%3A23%3A36.000Z%22%2C%22email%22%3A%22ahsueh1996%40gmail.com%22%2C%22profiles%22%3A%7B%22tax%22%3A%7B%22default%22%3A%22user-eedww24xbft%22%7D%2C%22trade%22%3A%7B%22default%22%3A%22user-ejs4xw9bbkg%22%7D%2C%22invest%22%3A%7B%22default%22%3A%22user-r2bl3nnqhso%22%7D%7D%2C%22client_canonical_ids%22%3A%7B%22tax%22%3A%7B%22default%22%3A%22person-bdiuyqifzp6yeg%22%7D%2C%22trade%22%3A%7B%22default%22%3A%22person-dnvo5jjaio1pfq%22%7D%2C%22invest%22%3A%7B%22default%22%3A%22person-1p_oiha5naqupq%22%7D%7D%2C%22suspended_profiles%22%3A%7B%7D%7D',
    'IR_5571': '1735934383548%7C0%7C1735934383548%7C%7C',
    'ab.storage.deviceId.80ec85f3-36f6-4cc8-8401-81fb1619363d': 'g%3A26157de1-4856-dbfa-e484-f715e455a091%7Ce%3Aundefined%7Cc%3A1734911250207%7Cl%3A1735934384547',
    'ab.storage.userId.80ec85f3-36f6-4cc8-8401-81fb1619363d': 'g%3Aidentity-mlJ2tNCvkG3B3O36zi62sL0ODOU%7Ce%3Aundefined%7Cc%3A1734911250205%7Cl%3A1735934384547',
    'ab.storage.sessionId.80ec85f3-36f6-4cc8-8401-81fb1619363d': 'g%3Af4bc6009-82e0-4757-e023-792c50e07664%7Ce%3A1735934684560%7Cc%3A1735934384547%7Cl%3A1735934384560',
    '_dd_s': 'rum=0&expire=1735935690298',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer eyJhbGc......HRheC53cm3ifzBXaqTc_1cHS1oCZkyA533OEu32wFClqvoYzBJ_SkQqLlBQZ42ZV4def8qaDLCgJ......WaTsR3YvuoVs0c3jonszsAUayRuUYyjpBCL3HDDOZCRX9-lLZ88T4qYdfzzdGui7dvG2dyibbFSGCXAKzl8nWmEh2BNJo_YMubI62Ajfog',
    'content-type': 'application/json',
    # 'cookie': 'ws_global_visitor_id=5f51a681-3c43-4db9-9342-ed24798724c0; _session_id=84a4778702c147021fa8c0973734a285; _tt_enable_cookie=1; IR_gbd=wealthsimple.com; wssdi=41521b683939e86c668e7b34745c8461; ajs_user_id=user-r2bl3nnqhso; _ttp=ENEQvi1xSYojKm8TnqLykO1CCs0.tt.1; _cfuvid=N2itggAkvLojQXcSHSMq.6czzTsnSIBcgN4xDefRWRw-1735929829001-0.0.1.1-604800000; ws_global_visitor_id=2f6df067-a378-44d7-a510-d0a63bf4a3c9; ajs_anonymous_id=aea41d51-0363-4b63-84e9-8157535b9335; _oauth2_access_v2=%7B%22access_token%22%3A%22eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJpZGVudGl0eS1tbEoydE5DdmtHM0IzTzM2emk2MnNMME9ET1UiLCJleHAiOjE3MzU5MzU4MTYsImlhdCI6MTczNTkzNDAxNiwianRpIjoiX1BfWnVNcHpNTG9OdlpLVDNqUkE5WC1Fd0EwVmVXRjRja3FKejltYU8tYyIsImNsaWVudF9pZCI6IjRkYTUzYWMyYjAzMjI1YmVkMTU1MGViYThlNDYxMWUwODZjN2I5MDVhMzg1NWU2ZWQxMmVhMDhjMjQ2NzU4ZmEiLCJzY29wZSI6ImludmVzdC5yZWFkIGludmVzdC53cml0ZSB0cmFkZS5yZWFkIHRyYWRlLndyaXRlIHRheC5yZWFkIHRheC53cml0ZSJ9.0j73lzNrJVRSjhMp6a1yq3ifzBXaqTc_1cHS1oCZAo5YyuyhvXeS8AZqvbx-YGwfXIWHjiyL7OzPuwBdceZVVQXePEtA1axkyA533OEu32wFClqvoYzBJ_SkQqLlBQiIz_lRjnDd1ncECuDJo6S75l2_4YaogHIabYYiZ42ZFtyrC4qwPn6OTbZV7jMXpI0nEpqGMT_hAV4def8qaDLCgJEIT2b0lRJptXCCQqMpwap9WaTsR3YvuoVs0c3jonszsAUayRuUYyjpBCL3HDDOZCRX9-lLZ88T4qYdfzzdGui7dvG2dyibbFSGCXAKzl8nWmEh2BNJo_YMubI62Ajfog%22%2C%22token_type%22%3A%22Bearer%22%2C%22expires_in%22%3A1800%2C%22refresh_token%22%3A%22EIcyM8ai-uNNPrj2bSojr_y6FrWcpAcUbC8t8G87PoM%22%2C%22scope%22%3A%22invest.read%20invest.write%20trade.read%20trade.write%20tax.read%20tax.write%22%2C%22created_at%22%3A1735934016%2C%22okta_group_claims%22%3A%5B%5D%2C%22identity_canonical_id%22%3A%22identity-mlJ2tNCvkG3B3O36zi62sL0ODOU%22%2C%22clock_skew%22%3A%7B%22skewed%22%3Afalse%7D%2C%22expires_at%22%3A%222025-01-03T20%3A23%3A36.000Z%22%2C%22email%22%3A%22ahsueh1996%40gmail.com%22%2C%22profiles%22%3A%7B%22tax%22%3A%7B%22default%22%3A%22user-eedww24xbft%22%7D%2C%22trade%22%3A%7B%22default%22%3A%22user-ejs4xw9bbkg%22%7D%2C%22invest%22%3A%7B%22default%22%3A%22user-r2bl3nnqhso%22%7D%7D%2C%22client_canonical_ids%22%3A%7B%22tax%22%3A%7B%22default%22%3A%22person-bdiuyqifzp6yeg%22%7D%2C%22trade%22%3A%7B%22default%22%3A%22person-dnvo5jjaio1pfq%22%7D%2C%22invest%22%3A%7B%22default%22%3A%22person-1p_oiha5naqupq%22%7D%7D%2C%22suspended_profiles%22%3A%7B%7D%7D; IR_5571=1735934383548%7C0%7C1735934383548%7C%7C; ab.storage.deviceId.80ec85f3-36f6-4cc8-8401-81fb1619363d=g%3A26157de1-4856-dbfa-e484-f715e455a091%7Ce%3Aundefined%7Cc%3A1734911250207%7Cl%3A1735934384547; ab.storage.userId.80ec85f3-36f6-4cc8-8401-81fb1619363d=g%3Aidentity-mlJ2tNCvkG3B3O36zi62sL0ODOU%7Ce%3Aundefined%7Cc%3A1734911250205%7Cl%3A1735934384547; ab.storage.sessionId.80ec85f3-36f6-4cc8-8401-81fb1619363d=g%3Af4bc6009-82e0-4757-e023-792c50e07664%7Ce%3A1735934684560%7Cc%3A1735934384547%7Cl%3A1735934384560; _dd_s=rum=0&expire=1735935690298',
    'origin': 'https://my.wealthsimple.com',
    'priority': 'u=1, i',
    'referer': 'https://my.wealthsimple.com/app/security-details/sec-s-86f44a72211b4effaf2bd1bafddadf1e?account=non-registered-OIzSXMKX6w',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'x-platform-os': 'web',
    'x-ws-api-version': '12',
    'x-ws-device-id': '41521b683939e86c668e7b34745c8461',
    'x-ws-locale': 'en-CA',
    'x-ws-profile': 'trade',
}

json_data = {
    'operationName': 'SoOrdersOrderCreate',
    'variables': {
        'input': {
            'canonicalAccountId': 'Secret... MORE SECRET',
            'externalId': 'order-189b089d-68e9-4064-97f8-b8ddfe288fd4',
            'executionType': 'LIMIT',
            'orderType': 'BUY_QUANTITY',
            'quantity': 1,
            'securityId': 'sec-s-86f44a72211b4effaf2bd1bafddadf1e',
            'timeInForce': 'DAY',
            'limitPrice': 8,
            'extendedHoursOrder': False,
        },
    },
    'query': 'mutation SoOrdersOrderCreate($input: SoOrders_CreateOrderInput!) {\n  soOrdersCreateOrder(input: $input) {\n    errors {\n      code\n      message\n      __typename\n    }\n    order {\n      orderId\n      createdAt\n      __typename\n    }\n    __typename\n  }\n}',
}

response = requests.post('https://my.wealthsimple.com/graphql', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"operationName":"SoOrdersOrderCreate","variables":{"input":{"canonicalAccountId":"non-registered-OIzSXMKX6w","externalId":"order-189b089d-68e9-4064-97f8-b8ddfe288fd4","executionType":"LIMIT","orderType":"BUY_QUANTITY","quantity":1,"securityId":"sec-s-86f44a72211b4effaf2bd1bafddadf1e","timeInForce":"DAY","limitPrice":8,"extendedHoursOrder":false}},"query":"mutation SoOrdersOrderCreate($input: SoOrders_CreateOrderInput!) {\\n  soOrdersCreateOrder(input: $input) {\\n    errors {\\n      code\\n      message\\n      __typename\\n    }\\n    order {\\n      orderId\\n      createdAt\\n      __typename\\n    }\\n    __typename\\n  }\\n}"}'
#response = requests.post('https://my.wealthsimple.com/graphql', cookies=cookies, headers=headers, data=data)


import copy
import uuid

LIMIT = 'LIMIT' 
FRACTIONAL = 'FRACTIONAL' # Cannot modify the order after it is placed
MARKET = 'MARKET'           # Cannot modify the order after it is placed
STOP_LIMIT = 'STOP_LIMIT'    # Cannot modify the order after it is placed

BUY_QUANTITY = 'BUY_QUANTITY'
SELL_QUANTITY = 'SELL_QUANTITY'
BUY_VALUE = 'BUY_VALUE'
SELL_VALUE = 'SELL_VALUE'

DAY = 'DAY'
GTC = 'UNTIL_CANCEL' # Cannot pair with extendedHoursOrder=True



# =================================================================================================
# =================================================================================================
# =================================================================================================
TODO = 'TODO'