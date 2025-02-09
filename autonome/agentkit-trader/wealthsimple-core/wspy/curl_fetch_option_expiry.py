"""
Goto the website and paste the curl command below to convert to python requests
**********************************************************************************************************************************
***** Remember to protect your privacy and remove any sensitive information before pasting the curl command to the website *******
************************************************ https://curlconverter.com/ ******************************************************

curl 'https://my.wealthsimple.com/graphql' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7,zh-CN;q=0.6,ko;q=0.5' \
  -H 'authorization: Bearer eyJhbGciOiJSUzI1NiJ9..--.........' \
  -H 'content-type: application/json' \
  -b 'IR_PI=7ac23cbe-1de5-11ee-8f81-650fe93bdcef%7C1713325456643; lang=en; __stripe_mid=042a30ea-8114-4764-8ca9-d5d9de59deb5036ccb; st_profile=8984583b-4dc9-4bcd-b34e-01e7d9668986; wst_luty=2023; session=.eJxljsEOgjAQBX_F7FVMaEukmHAgGrzqFxC63RIiUlMK1RD-3d48eJ43L7MCTs403j5ohBNIYlpLdUwZzwuUhgTKFDOmuUBVMCMYodJKQQI4O0ejb1pEO48-yvNE7kCkQ-DZWxn_P2p6DScuZC7T7Adf7TQF6yJaYafiUS2v1flZXZZQjbVdhs-wb2_3soQtgcF2Hemmj7XezbR9Af2tQE0.ZnnaxA.HFo_QgTIpJBRkJ5hIUnYTLKkXGs; ws_referrer_url=https://www.google.com/; ws_global_visitor_id=user_be27233bdbbd5d9cd21336ca58316316; wssdi=be27233bdbbd5d9cd21336ca58316316; ws_jurisdiction=CA; __cfruid=ab12f2914664edb63a656dcb18cf4c81f849885c-1730088880; _gcl_au=1.1.597370025.1733040259; _tt_enable_cookie=1; _ttp=2DSc5RSZH-8wmM8rALKCtdpVxvq.tt.1; IR_gbd=wealthsimple.com; _scid=n51vo54Z4XEyOmoQXQ8ampGiKy4shuOY; _sctr=1%7C1733029200000; ajs_user_id=user-r2bl3nnqhso; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2FPekbol7rMROh4Ketr4PuNz4uozog0iXE%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2Bm3H3HlqH8mvBpy7sFzRiESiTlG1g3G6Ka%2F%2FKsmGe%2By%2FJd7fskM2Trf%2FpXb8sKCbCOshzrZQPQ6Q%3D%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX1%2BQvXZ8n0ZJY8pRjPs5mcGXBwRmwPh2U3g%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX18wPQ3QXmJTUDgNrRLEkhML4scS9Tdmj9Q%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2B5QMk1uSRvdzEIIirnca45ZDfFAtcFNOg%3D; _gcl_aw=GCL.1733268910.CjwKCAiA9bq6BhAKEiwAH6bqoF5QvXLWsp76wwZL2S-Le_G4iKfod4Nz708jY0QjRcPwzkMoilzqsBoCa5IQAvD_BwE; _gcl_gs=2.1.k1$i1733268909$u183234660; _ga=GA1.1.561341326.1733040259; tatari-session-cookie=bff4bb99-0b59-c124-66b6-c6d46a9b18a5; _scid_r=rx1vo54Z4XEyOmoQXQ8ampGiKy4shuOYGPcn0A; _rdt_uuid=1733040259224.769f2a82-c0d4-452e-aa5f-7f2f3f105c4c; _ga_P3KV5N62JS=GS1.1.1733435040.5.0.1733435043.57.0.0; ajs_anonymous_id=164f2556-8f13-4ede-9802-432987a6d391; IR_5571=1733435047906%7C0%7C1733435047906%7C%7C; _session_id=84b58b713a44aa80454afc67ff69f5fd; _cfuvid=O5FwToeg47wcW9XAjsGk5BfsL6FMvYTZ8cegllP2zA4-1739051456976-0.0.1.1-604800000; _oauth2_access_v2=%7B%22access_token%22%3A%22eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJpZGVudGl0eS1tbEoydE5DdmtHM0IzTzM2emk2MnNMME9ET1UiLCJleHAiOjE3MzkwNTYzMTYsImlhdCI6MTczOTA1NDUxNiwianRpIjoiZWNja0RGRzUyUlRaR0o5S2FmM2JtWmRjbVg2TUw4LVAxU1JyQVRrZ2toYyIsImNsaWVudF9pZCI6IjRkYTUzYWMyYjAzMjI1YmVkMTU1MGViYThlNDYxMWUwODZjN2I5MDVhMzg1NWU2ZWQxMmVhMDhjMjQ2NzU4ZmEiLCJzY29wZSI6ImludmVzdC5yZWFkIGludmVzdC53cml0ZSB0cmFkZS5yZWFkIHRyYWRlLndyaXRlIHRheC5yZWFkIHRheC53cml0ZSJ9.DsOr2RppyHxcUtf4sUqznmbQlCdIvOJEj9FYDAidYX5fySogUa1Xox5kGWUQ62NKnWi3ABNmn3zEhU72OWIauDRoDfU7Q3kQS0Cn2fhsg46c3gTaiR2dVxBkeFaV2K-lmJKQh1eDCfgC3WAn8k5SqaTdhhjadM1J_T7_sQoXe524zaddrQruGYrLmiazdOnRBAofohFHFJjSiz4MWb4LQ-By3yTQnQBa1Qvs3opXWRsXFMq_Kue14CcBxgQokFmBTj9BQzrckw0V4RjQZ8Oy0auah1IF585cWo_1LO68u85ie4jOwi2C3C4KNQQ3MqOcnF0c5sUtT8lft48QUyA9gQ%22%2C%22token_type%22%3A%22Bearer%22%2C%22expires_in%22%3A1800%2C%22refresh_token%22%3A%22tqCHNItoH_dnYLUQEkcb44jxN4EJdbeepEpCHqFrEbE%22%2C%22scope%22%3A%22invest.read%20invest.write%20trade.read%20trade.write%20tax.read%20tax.write%22%2C%22created_at%22%3A1739054516%2C%22okta_group_claims%22%3A%5B%5D%2C%22identity_canonical_id%22%3A%22identity-mlJ2tNCvkG3B3O36zi62sL0ODOU%22%2C%22clock_skew%22%3A%7B%22skewed%22%3Afalse%7D%2C%22expires_at%22%3A%222025-02-08T23%3A11%3A56.000Z%22%2C%22email%22%3A%22ahsueh1996%40gmail.com%22%2C%22profiles%22%3A%7B%22tax%22%3A%7B%22default%22%3A%22user-eedww24xbft%22%7D%2C%22trade%22%3A%7B%22default%22%3A%22user-ejs4xw9bbkg%22%7D%2C%22invest%22%3A%7B%22default%22%3A%22user-r2bl3nnqhso%22%7D%7D%2C%22client_canonical_ids%22%3A%7B%22tax%22%3A%7B%22default%22%3A%22person-bdiuyqifzp6yeg%22%7D%2C%22trade%22%3A%7B%22default%22%3A%22person-dnvo5jjaio1pfq%22%7D%2C%22invest%22%3A%7B%22default%22%3A%22person-1p_oiha5naqupq%22%7D%7D%2C%22suspended_profiles%22%3A%7B%7D%7D; ab.storage.deviceId.80ec85f3-36f6-4cc8-8401-81fb1619363d=g%3A6e824410-75e3-b1cb-770b-22d8f3c7b3e2%7Ce%3Aundefined%7Cc%3A1729882007159%7Cl%3A1739054519952; ab.storage.userId.80ec85f3-36f6-4cc8-8401-81fb1619363d=g%3Aidentity-mlJ2tNCvkG3B3O36zi62sL0ODOU%7Ce%3Aundefined%7Cc%3A1729882007157%7Cl%3A1739054519953; ab.storage.sessionId.80ec85f3-36f6-4cc8-8401-81fb1619363d=g%3A92baef6f-ad39-55cd-5900-8ccd923dd6cc%7Ce%3A1739054820559%7Cc%3A1739054519951%7Cl%3A1739054520559; _dd_s=rum=0&expire=1739055429733' \
  -H 'origin: https://my.wealthsimple.com' \
  -H 'priority: u=1, i' \
  -H 'referer: https://my.wealthsimple.com/app/security-details/sec-s-27167ecbd81140fe9cdc02535f43174d?tab=option_chain&optionType=CALL' \
  -H 'sec-ch-ua: "Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"' \
  -H 'sec-ch-ua-mobile: ?1' \
  -H 'sec-ch-ua-platform: "Android"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36' \
  -H 'x-platform-os: web' \
  -H 'x-ws-api-version: 12' \
  -H 'x-ws-device-id: be27233bdbbd5d9cd21336ca58316316' \
  -H 'x-ws-locale: en-CA' \
  -H 'x-ws-profile: trade' \
  --data-raw $'{"operationName":"FetchOptionExpirationDates","variables":{"securityId":"sec-s-27167ecbd81140fe9cdc02535f43174d","minDate":"2025-02-08","maxDate":"2028-02-08"},"query":"query FetchOptionExpirationDates($securityId: ID\u0021, $minDate: Date\u0021, $maxDate: Date\u0021) {\\n  security(id: $securityId) {\\n    id\\n    optionExpirationDates(minDate: $minDate, maxDate: $maxDate) {\\n      ...OptionExpirationDates\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n\\nfragment OptionExpirationDates on OptionExpirationDates {\\n  expirationDates\\n  __typename\\n}"}'

minDate: "2025-02-08"  required but you can't look back in time
maxDate: "2028-02-08"  required, can be long into the future
minDate < maxDate
suggest to use hardcoded minDate and maxDate:
  1111-11-11 = minDate < maxDate = 9999-11-11
"""

import requests

cookies = {
    'IR_PI': '7ac23cbe-1de5-11ee-8f81-650fe93bdcef%7C1713325456643',
    'lang': 'en',
    '__stripe_mid': '042a30ea-8114-4764-8ca9-d5d9de59deb5036ccb',
    'st_profile': '8984583b-4dc9-4bcd-b34e-01e7d9668986',
    'wst_luty': '2023',
    'session': '.eJxljsEOgjAQBX_F7FVMaEukmHAgGrzqFxC63RIiUlMK1RD-3d48eJ43L7MCTs403j5ohBNIYlpLdUwZzwuUhgTKFDOmuUBVMCMYodJKQQI4O0ejb1pEO48-yvNE7kCkQ-DZWxn_P2p6DScuZC7T7Adf7TQF6yJaYafiUS2v1flZXZZQjbVdhs-wb2_3soQtgcF2Hemmj7XezbR9Af2tQE0.ZnnaxA.HFo_QgTIpJBRkJ5hIUnYTLKkXGs',
    'ws_referrer_url': 'https://www.google.com/',
    'ws_global_visitor_id': 'user_be27233bdbbd5d9cd21336ca58316316',
    'wssdi': 'be27233bdbbd5d9cd21336ca58316316',
    'ws_jurisdiction': 'CA',
    '__cfruid': 'ab12f2914664edb63a656dcb18cf4c81f849885c-1730088880',
    '_gcl_au': '1.1.597370025.1733040259',
    '_tt_enable_cookie': '1',
    '_ttp': '2DSc5RSZH-8wmM8rALKCtdpVxvq.tt.1',
    'IR_gbd': 'wealthsimple.com',
    '_scid': 'n51vo54Z4XEyOmoQXQ8ampGiKy4shuOY',
    '_sctr': '1%7C1733029200000',
    'ajs_user_id': 'user-r2bl3nnqhso',
    'rl_user_id': 'RudderEncrypt%3AU2FsdGVkX1%2FPekbol7rMROh4Ketr4PuNz4uozog0iXE%3D',
    'rl_anonymous_id': 'RudderEncrypt%3AU2FsdGVkX1%2Bm3H3HlqH8mvBpy7sFzRiESiTlG1g3G6Ka%2F%2FKsmGe%2By%2FJd7fskM2Trf%2FpXb8sKCbCOshzrZQPQ6Q%3D%3D',
    'rl_group_id': 'RudderEncrypt%3AU2FsdGVkX1%2BQvXZ8n0ZJY8pRjPs5mcGXBwRmwPh2U3g%3D',
    'rl_trait': 'RudderEncrypt%3AU2FsdGVkX18wPQ3QXmJTUDgNrRLEkhML4scS9Tdmj9Q%3D',
    'rl_group_trait': 'RudderEncrypt%3AU2FsdGVkX1%2B5QMk1uSRvdzEIIirnca45ZDfFAtcFNOg%3D',
    '_gcl_aw': 'GCL.1733268910.CjwKCAiA9bq6BhAKEiwAH6bqoF5QvXLWsp76wwZL2S-Le_G4iKfod4Nz708jY0QjRcPwzkMoilzqsBoCa5IQAvD_BwE',
    '_gcl_gs': '2.1.k1$i1733268909$u183234660',
    '_ga': 'GA1.1.561341326.1733040259',
    'tatari-session-cookie': 'bff4bb99-0b59-c124-66b6-c6d46a9b18a5',
    '_scid_r': 'rx1vo54Z4XEyOmoQXQ8ampGiKy4shuOYGPcn0A',
    '_rdt_uuid': '1733040259224.769f2a82-c0d4-452e-aa5f-7f2f3f105c4c',
    '_ga_P3KV5N62JS': 'GS1.1.1733435040.5.0.1733435043.57.0.0',
    'ajs_anonymous_id': '164f2556-8f13-4ede-9802-432987a6d391',
    'IR_5571': '1733435047906%7C0%7C1733435047906%7C%7C',
    '_session_id': '84b58b713a44aa80454afc67ff69f5fd',
    '_cfuvid': 'O5FwToeg47wcW9XAjsGk5BfsL6FMvYTZ8cegllP2zA4-1739051456976-0.0.1.1-604800000',
    '_oauth2_access_v2': '%7B%22access_token%22%3A%22eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJpZGVudGl0eS1tbEoydE5DdmtHM0IzTzM2emk2MnNMME9ET1UiLCJleHAiOjE3MzkwNTYzMTYsImlhdCI6MTczOTA1NDUxNiwianRpIjoiZWNja0RGRzUyUlRaR0o5S2FmM2JtWmRjbVg2TUw4LVAxU1JyQVRrZ2toYyIsImNsaWVudF9pZCI6IjRkYTUzYWMyYjAzMjI1YmVkMTU1MGViYThlNDYxMWUwODZjN2I5MDVhMzg1NWU2ZWQxMmVhMDhjMjQ2NzU4ZmEiLCJzY29wZSI6ImludmVzdC5yZWFkIGludmVzdC53cml0ZSB0cmFkZS5yZWFkIHRyYWRlLndyaXRlIHRheC5yZWFkIHRheC53cml0ZSJ9.DsOr2RppyHxcUtf4sUqznmbQlCdIvOJEj9FYDAidYX5fySogUa1Xox5kGWUQ62NKnWi3ABNmn3zEhU72OWIauDRoDfU7Q3kQS0Cn2fhsg46c3gTaiR2dVxBkeFaV2K-lmJKQh1eDCfgC3WAn8k5SqaTdhhjadM1J_T7_sQoXe524zaddrQruGYrLmiazdOnRBAofohFHFJjSiz4MWb4LQ-By3yTQnQBa1Qvs3opXWRsXFMq_Kue14CcBxgQokFmBTj9BQzrckw0V4RjQZ8Oy0auah1IF585cWo_1LO68u85ie4jOwi2C3C4KNQQ3MqOcnF0c5sUtT8lft48QUyA9gQ%22%2C%22token_type%22%3A%22Bearer%22%2C%22expires_in%22%3A1800%2C%22refresh_token%22%3A%22tqCHNItoH_dnYLUQEkcb44jxN4EJdbeepEpCHqFrEbE%22%2C%22scope%22%3A%22invest.read%20invest.write%20trade.read%20trade.write%20tax.read%20tax.write%22%2C%22created_at%22%3A1739054516%2C%22okta_group_claims%22%3A%5B%5D%2C%22identity_canonical_id%22%3A%22identity-mlJ2tNCvkG3B3O36zi62sL0ODOU%22%2C%22clock_skew%22%3A%7B%22skewed%22%3Afalse%7D%2C%22expires_at%22%3A%222025-02-08T23%3A11%3A56.000Z%22%2C%22email%22%3A%22ahsueh1996%40gmail.com%22%2C%22profiles%22%3A%7B%22tax%22%3A%7B%22default%22%3A%22user-eedww24xbft%22%7D%2C%22trade%22%3A%7B%22default%22%3A%22user-ejs4xw9bbkg%22%7D%2C%22invest%22%3A%7B%22default%22%3A%22user-r2bl3nnqhso%22%7D%7D%2C%22client_canonical_ids%22%3A%7B%22tax%22%3A%7B%22default%22%3A%22person-bdiuyqifzp6yeg%22%7D%2C%22trade%22%3A%7B%22default%22%3A%22person-dnvo5jjaio1pfq%22%7D%2C%22invest%22%3A%7B%22default%22%3A%22person-1p_oiha5naqupq%22%7D%7D%2C%22suspended_profiles%22%3A%7B%7D%7D',
    'ab.storage.deviceId.80ec85f3-36f6-4cc8-8401-81fb1619363d': 'g%3A6e824410-75e3-b1cb-770b-22d8f3c7b3e2%7Ce%3Aundefined%7Cc%3A1729882007159%7Cl%3A1739054519952',
    'ab.storage.userId.80ec85f3-36f6-4cc8-8401-81fb1619363d': 'g%3Aidentity-mlJ2tNCvkG3B3O36zi62sL0ODOU%7Ce%3Aundefined%7Cc%3A1729882007157%7Cl%3A1739054519953',
    'ab.storage.sessionId.80ec85f3-36f6-4cc8-8401-81fb1619363d': 'g%3A92baef6f-ad39-55cd-5900-8ccd923dd6cc%7Ce%3A1739054820559%7Cc%3A1739054519951%7Cl%3A1739054520559',
    '_dd_s': 'rum=0&expire=1739055429733',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7,zh-CN;q=0.6,ko;q=0.5',
    'authorization': 'Bearer eyJhbGciOiJSUzI1NiJ9..--.........',
    'content-type': 'application/json',
    'origin': 'https://my.wealthsimple.com',
    'priority': 'u=1, i',
    'referer': 'https://my.wealthsimple.com/app/security-details/sec-s-27167ecbd81140fe9cdc02535f43174d?tab=option_chain&optionType=CALL',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36',
    'x-platform-os': 'web',
    'x-ws-api-version': '12',
    'x-ws-device-id': 'be27233bdbbd5d9cd21336ca58316316',
    'x-ws-locale': 'en-CA',
    'x-ws-profile': 'trade',
    # 'cookie': 'IR_PI=7ac23cbe-1de5-11ee-8f81-650fe93bdcef%7C1713325456643; lang=en; __stripe_mid=042a30ea-8114-4764-8ca9-d5d9de59deb5036ccb; st_profile=8984583b-4dc9-4bcd-b34e-01e7d9668986; wst_luty=2023; session=.eJxljsEOgjAQBX_F7FVMaEukmHAgGrzqFxC63RIiUlMK1RD-3d48eJ43L7MCTs403j5ohBNIYlpLdUwZzwuUhgTKFDOmuUBVMCMYodJKQQI4O0ejb1pEO48-yvNE7kCkQ-DZWxn_P2p6DScuZC7T7Adf7TQF6yJaYafiUS2v1flZXZZQjbVdhs-wb2_3soQtgcF2Hemmj7XezbR9Af2tQE0.ZnnaxA.HFo_QgTIpJBRkJ5hIUnYTLKkXGs; ws_referrer_url=https://www.google.com/; ws_global_visitor_id=user_be27233bdbbd5d9cd21336ca58316316; wssdi=be27233bdbbd5d9cd21336ca58316316; ws_jurisdiction=CA; __cfruid=ab12f2914664edb63a656dcb18cf4c81f849885c-1730088880; _gcl_au=1.1.597370025.1733040259; _tt_enable_cookie=1; _ttp=2DSc5RSZH-8wmM8rALKCtdpVxvq.tt.1; IR_gbd=wealthsimple.com; _scid=n51vo54Z4XEyOmoQXQ8ampGiKy4shuOY; _sctr=1%7C1733029200000; ajs_user_id=user-r2bl3nnqhso; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2FPekbol7rMROh4Ketr4PuNz4uozog0iXE%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2Bm3H3HlqH8mvBpy7sFzRiESiTlG1g3G6Ka%2F%2FKsmGe%2By%2FJd7fskM2Trf%2FpXb8sKCbCOshzrZQPQ6Q%3D%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX1%2BQvXZ8n0ZJY8pRjPs5mcGXBwRmwPh2U3g%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX18wPQ3QXmJTUDgNrRLEkhML4scS9Tdmj9Q%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2B5QMk1uSRvdzEIIirnca45ZDfFAtcFNOg%3D; _gcl_aw=GCL.1733268910.CjwKCAiA9bq6BhAKEiwAH6bqoF5QvXLWsp76wwZL2S-Le_G4iKfod4Nz708jY0QjRcPwzkMoilzqsBoCa5IQAvD_BwE; _gcl_gs=2.1.k1$i1733268909$u183234660; _ga=GA1.1.561341326.1733040259; tatari-session-cookie=bff4bb99-0b59-c124-66b6-c6d46a9b18a5; _scid_r=rx1vo54Z4XEyOmoQXQ8ampGiKy4shuOYGPcn0A; _rdt_uuid=1733040259224.769f2a82-c0d4-452e-aa5f-7f2f3f105c4c; _ga_P3KV5N62JS=GS1.1.1733435040.5.0.1733435043.57.0.0; ajs_anonymous_id=164f2556-8f13-4ede-9802-432987a6d391; IR_5571=1733435047906%7C0%7C1733435047906%7C%7C; _session_id=84b58b713a44aa80454afc67ff69f5fd; _cfuvid=O5FwToeg47wcW9XAjsGk5BfsL6FMvYTZ8cegllP2zA4-1739051456976-0.0.1.1-604800000; _oauth2_access_v2=%7B%22access_token%22%3A%22eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJpZGVudGl0eS1tbEoydE5DdmtHM0IzTzM2emk2MnNMME9ET1UiLCJleHAiOjE3MzkwNTYzMTYsImlhdCI6MTczOTA1NDUxNiwianRpIjoiZWNja0RGRzUyUlRaR0o5S2FmM2JtWmRjbVg2TUw4LVAxU1JyQVRrZ2toYyIsImNsaWVudF9pZCI6IjRkYTUzYWMyYjAzMjI1YmVkMTU1MGViYThlNDYxMWUwODZjN2I5MDVhMzg1NWU2ZWQxMmVhMDhjMjQ2NzU4ZmEiLCJzY29wZSI6ImludmVzdC5yZWFkIGludmVzdC53cml0ZSB0cmFkZS5yZWFkIHRyYWRlLndyaXRlIHRheC5yZWFkIHRheC53cml0ZSJ9.DsOr2RppyHxcUtf4sUqznmbQlCdIvOJEj9FYDAidYX5fySogUa1Xox5kGWUQ62NKnWi3ABNmn3zEhU72OWIauDRoDfU7Q3kQS0Cn2fhsg46c3gTaiR2dVxBkeFaV2K-lmJKQh1eDCfgC3WAn8k5SqaTdhhjadM1J_T7_sQoXe524zaddrQruGYrLmiazdOnRBAofohFHFJjSiz4MWb4LQ-By3yTQnQBa1Qvs3opXWRsXFMq_Kue14CcBxgQokFmBTj9BQzrckw0V4RjQZ8Oy0auah1IF585cWo_1LO68u85ie4jOwi2C3C4KNQQ3MqOcnF0c5sUtT8lft48QUyA9gQ%22%2C%22token_type%22%3A%22Bearer%22%2C%22expires_in%22%3A1800%2C%22refresh_token%22%3A%22tqCHNItoH_dnYLUQEkcb44jxN4EJdbeepEpCHqFrEbE%22%2C%22scope%22%3A%22invest.read%20invest.write%20trade.read%20trade.write%20tax.read%20tax.write%22%2C%22created_at%22%3A1739054516%2C%22okta_group_claims%22%3A%5B%5D%2C%22identity_canonical_id%22%3A%22identity-mlJ2tNCvkG3B3O36zi62sL0ODOU%22%2C%22clock_skew%22%3A%7B%22skewed%22%3Afalse%7D%2C%22expires_at%22%3A%222025-02-08T23%3A11%3A56.000Z%22%2C%22email%22%3A%22ahsueh1996%40gmail.com%22%2C%22profiles%22%3A%7B%22tax%22%3A%7B%22default%22%3A%22user-eedww24xbft%22%7D%2C%22trade%22%3A%7B%22default%22%3A%22user-ejs4xw9bbkg%22%7D%2C%22invest%22%3A%7B%22default%22%3A%22user-r2bl3nnqhso%22%7D%7D%2C%22client_canonical_ids%22%3A%7B%22tax%22%3A%7B%22default%22%3A%22person-bdiuyqifzp6yeg%22%7D%2C%22trade%22%3A%7B%22default%22%3A%22person-dnvo5jjaio1pfq%22%7D%2C%22invest%22%3A%7B%22default%22%3A%22person-1p_oiha5naqupq%22%7D%7D%2C%22suspended_profiles%22%3A%7B%7D%7D; ab.storage.deviceId.80ec85f3-36f6-4cc8-8401-81fb1619363d=g%3A6e824410-75e3-b1cb-770b-22d8f3c7b3e2%7Ce%3Aundefined%7Cc%3A1729882007159%7Cl%3A1739054519952; ab.storage.userId.80ec85f3-36f6-4cc8-8401-81fb1619363d=g%3Aidentity-mlJ2tNCvkG3B3O36zi62sL0ODOU%7Ce%3Aundefined%7Cc%3A1729882007157%7Cl%3A1739054519953; ab.storage.sessionId.80ec85f3-36f6-4cc8-8401-81fb1619363d=g%3A92baef6f-ad39-55cd-5900-8ccd923dd6cc%7Ce%3A1739054820559%7Cc%3A1739054519951%7Cl%3A1739054520559; _dd_s=rum=0&expire=1739055429733',
}

json_data = {
    'operationName': 'FetchOptionExpirationDates',
    'variables': {
        'securityId': 'sec-s-27167ecbd81140fe9cdc02535f43174d',
        'minDate': '1111-02-08',
        'maxDate': '9999-02-08',
    },
    'query': 'query FetchOptionExpirationDates($securityId: ID!, $minDate: Date!, $maxDate: Date!) {\n  security(id: $securityId) {\n    id\n    optionExpirationDates(minDate: $minDate, maxDate: $maxDate) {\n      ...OptionExpirationDates\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment OptionExpirationDates on OptionExpirationDates {\n  expirationDates\n  __typename\n}',
}

response = requests.post('https://my.wealthsimple.com/graphql', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"operationName":"FetchOptionExpirationDates","variables":{"securityId":"sec-s-27167ecbd81140fe9cdc02535f43174d","minDate":"2025-02-08","maxDate":"2028-02-08"},"query":"query FetchOptionExpirationDates($securityId: ID!, $minDate: Date!, $maxDate: Date!) {\\n  security(id: $securityId) {\\n    id\\n    optionExpirationDates(minDate: $minDate, maxDate: $maxDate) {\\n      ...OptionExpirationDates\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n\\nfragment OptionExpirationDates on OptionExpirationDates {\\n  expirationDates\\n  __typename\\n}"}'
#response = requests.post('https://my.wealthsimple.com/graphql', cookies=cookies, headers=headers, data=data)

import copy
def create_request_json(security_id):
    global json_data
    json_data = copy.deepcopy(json_data)
    json_data['variables']['securityId'] = security_id
    return json_data

"""
{
    "data": {
        "security": {
            "id": "sec-s-27167ecbd81140fe9cdc02535f43174d",
            "optionExpirationDates": {
                "expirationDates": [
                    "2025-02-10",
                    "2025-02-11",
                    "2025-02-12",
                    "2025-02-13",
                    "2025-02-14",
                    "2025-02-18",
                    "2025-02-19",
                    "2025-02-20",
                    "2025-02-21",
                    "2025-02-28",
                    "2025-03-07",
                    "2025-03-14",
                    "2025-03-21",
                    "2025-03-28",
                    "2025-03-31",
                    "2025-04-17",
                    "2025-04-30",
                    "2025-05-16",
                    "2025-05-30",
                    "2025-06-20",
                    "2025-06-30",
                    "2025-07-18",
                    "2025-07-31",
                    "2025-08-15",
                    "2025-09-19",
                    "2025-09-30",
                    "2025-12-19",
                    "2025-12-31",
                    "2026-01-16",
                    "2026-03-20",
                    "2026-06-18",
                    "2026-12-18",
                    "2027-01-15",
                    "2027-12-17"
                ],
                "__typename": "OptionExpirationDates"
            },
            "__typename": "Security"
        }
    }
}
"""