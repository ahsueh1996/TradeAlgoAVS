"""
Goto the website and paste the curl command below to convert to python requests
**********************************************************************************************************************************
***** Remember to protect your privacy and remove any sensitive information before pasting the curl command to the website *******
************************************************ https://curlconverter.com/ ******************************************************

curl 'https://my.wealthsimple.com/graphql' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7,zh-CN;q=0.6,ko;q=0.5' \
  -H 'authorization: Bearer eyJhbGciOiJSU....mlhdCI6MTczOTA1MTQyMSwianRpIjoiQ2R4ZDM2M2dTSH......udF9pZCI6IjRkYTUzYWMyYjAzMjI1......iLCJzY29wZSI6I.........0YLxh1s5CgX1zgEFNhPjkzuweYWmUE2-fTg1W-9xYykqB53xXeVCGxSiWbU28r3gRtO4U6eEAS4II8r4Hsd9Ihy43_ZVvKRWSaw0ITgrTQaKfT0Q7t8mqh84g' \
  -H 'content-type: application/json' \
  -b 'IR_PI=7ac23cbe-1de5-11ee-8f81-650fe93bdcef%7C1713325456643; lang=en; __stripe_mid=042a30ea-8114-4764-8ca9-d5d9de59deb5036ccb; st_profile=8984583b-4dc9-4bcd-b34e-01e7d9668986; wst_luty=2023; session=.eJxljsEOgjAQBX_F7FVMaEukmHAgGrzqFxC63RIiUlMK1RD-3d48eJ43L7MCTs403j5ohBNIYlpLdUwZzwuUhgTKFDOmuUBVMCMYodJKQQI4O0ejb1pEO48-yvNE7kCkQ-DZWxn_P2p6DScuZC7T7Adf7TQF6yJaYafiUS2v1flZXZZQjbVdhs-wb2_3soQtgcF2Hemmj7XezbR9Af2tQE0.ZnnaxA.HFo_QgTIpJBRkJ5hIUnYTLKkXGs; ws_referrer_url=https://www.google.com/; ws_global_visitor_id=user_be27233bdbbd5d9cd21336ca58316316; wssdi=be27233bdbbd5d9cd21336ca58316316; ws_jurisdiction=CA; __cfruid=ab12f2914664edb63a656dcb18cf4c81f849885c-1730088880; _gcl_au=1.1.597370025.1733040259; _tt_enable_cookie=1; _ttp=2DSc5RSZH-8wmM8rALKCtdpVxvq.tt.1; IR_gbd=wealthsimple.com; _scid=n51vo54Z4XEyOmoQXQ8ampGiKy4shuOY; _sctr=1%7C1733029200000; ajs_user_id=user-r2bl3nnqhso; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2FPekbol7rMROh4Ketr4PuNz4uozog0iXE%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2Bm3H3HlqH8mvBpy7sFzRiESiTlG1g3G6Ka%2F%2FKsmGe%2By%2FJd7fskM2Trf%2FpXb8sKCbCOshzrZQPQ6Q%3D%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX1%2BQvXZ8n0ZJY8pRjPs5mcGXBwRmwPh2U3g%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX18wPQ3QXmJTUDgNrRLEkhML4scS9Tdmj9Q%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2B5QMk1uSRvdzEIIirnca45ZDfFAtcFNOg%3D; _gcl_aw=GCL.1733268910.CjwKCAiA9bq6BhAKEiwAH6bqoF5QvXLWsp76wwZL2S-Le_G4iKfod4Nz708jY0QjRcPwzkMoilzqsBoCa5IQAvD_BwE; _gcl_gs=2.1.k1$i1733268909$u183234660; _ga=GA1.1.561341326.1733040259; tatari-session-cookie=bff4bb99-0b59-c124-66b6-c6d46a9b18a5; _scid_r=rx1vo54Z4XEyOmoQXQ8ampGiKy4shuOYGPcn0A; _rdt_uuid=1733040259224.769f2a82-c0d4-452e-aa5f-7f2f3f105c4c; _ga_P3KV5N62JS=GS1.1.1733435040.5.0.1733435043.57.0.0; ajs_anonymous_id=164f2556-8f13-4ede-9802-432987a6d391; IR_5571=1733435047906%7C0%7C1733435047906%7C%7C; _oauth2_access_v2=%7B%22access_token%22%3A%22eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJpZGVudGl0eS1tbEoydE5DdmtHM0IzTzM2emk2MnNMME9ET1UiLCJleHAiOjE3MzkwNTMyMjEsImlhdCI6MTczOTA1MTQyMSwianRpIjoiQ2R4ZDM2M2dTSHNZQXFibHdOZmdDdllnLWVRVTY5VWNTMVRfVzd5RGtHRSIsImNsaWVudF9pZCI6IjRkYTUzYWMyYjAzMjI1YmVkMTU1MGViYThlNDYxMWUwODZjN2I5MDVhMzg1NWU2ZWQxMmVhMDhjMjQ2NzU4ZmEiLCJzY29wZSI6ImludmVzdC5yZWFkIGludmVzdC53cml0ZSB0cmFkZS5yZWFkIHRyYWRlLndyaXRlIHRheC5yZWFkIHRheC53cml0ZSJ9.flsSuG29bJ-EGLO5R-EmAmwrQbONMpeMV4EF1zw6n2FDVc7wUPRnq87OE8lsktelwk7EG82HTMLpCA4frgX8QaGyc48O-Wdl-Q6C3EkkR8RtluvykSBverCnPdHyF3K-uVbmWAGC8rPqLiNL-R9Z3_1cFwrKss6u5qQnyUUbUD7ldutHbgHSPIVpQ1W51UbPs8XcnhJfIeTCQd0o89KQshykCZp8Q0YLxh1s5CgX1zgEFNhPjkzuweYWmUE2-fTg1W-9xYykqB53xXeVCGxSiWbU28r3gRtO4U6eEAS4II8r4Hsd9Ihy43_ZVvKRWSaw0ITgrTQaKfT0Q7t8mqh84g%22%2C%22token_type%22%3A%22Bearer%22%2C%22expires_in%22%3A1800%2C%22refresh_token%22%3A%22kdXhbhmTaD82z2q69yO8zgWJ5nsKsnMYMPAIIHyh1zA%22%2C%22scope%22%3A%22invest.read%20invest.write%20trade.read%20trade.write%20tax.read%20tax.write%22%2C%22created_at%22%3A1739051421%2C%22okta_group_claims%22%3A%5B%5D%2C%22identity_canonical_id%22%3A%22identity-mlJ2tNCvkG3B3O36zi62sL0ODOU%22%2C%22clock_skew%22%3A%7B%22skewed%22%3Afalse%7D%2C%22expires_at%22%3A%222025-02-08T22%3A20%3A21.000Z%22%2C%22email%22%3A%22ahsueh1996%40gmail.com%22%2C%22profiles%22%3A%7B%22tax%22%3A%7B%22default%22%3A%22user-eedww24xbft%22%7D%2C%22trade%22%3A%7B%22default%22%3A%22user-ejs4xw9bbkg%22%7D%2C%22invest%22%3A%7B%22default%22%3A%22user-r2bl3nnqhso%22%7D%7D%2C%22client_canonical_ids%22%3A%7B%22tax%22%3A%7B%22default%22%3A%22person-bdiuyqifzp6yeg%22%7D%2C%22trade%22%3A%7B%22default%22%3A%22person-dnvo5jjaio1pfq%22%7D%2C%22invest%22%3A%7B%22default%22%3A%22person-1p_oiha5naqupq%22%7D%7D%2C%22suspended_profiles%22%3A%7B%7D%7D; _session_id=84b58b713a44aa80454afc67ff69f5fd; ab.storage.deviceId.80ec85f3-36f6-4cc8-8401-81fb1619363d=g%3A6e824410-75e3-b1cb-770b-22d8f3c7b3e2%7Ce%3Aundefined%7Cc%3A1729882007159%7Cl%3A1739051424752; ab.storage.userId.80ec85f3-36f6-4cc8-8401-81fb1619363d=g%3Aidentity-mlJ2tNCvkG3B3O36zi62sL0ODOU%7Ce%3Aundefined%7Cc%3A1729882007157%7Cl%3A1739051424753; ab.storage.sessionId.80ec85f3-36f6-4cc8-8401-81fb1619363d=g%3Ab5c29665-6202-a2f9-bb63-66d9c3d5c035%7Ce%3A1739051725605%7Cc%3A1739051424751%7Cl%3A1739051425605; _cfuvid=O5FwToeg47wcW9XAjsGk5BfsL6FMvYTZ8cegllP2zA4-1739051456976-0.0.1.1-604800000; _dd_s=rum=0&expire=1739052360067' \
  -H 'origin: https://my.wealthsimple.com' \
  -H 'priority: u=1, i' \
  -H 'referer: https://my.wealthsimple.com/app/security-details/sec-s-27167ecbd81140fe9cdc02535f43174d?tab=option_chain&optionType=CALL&expiryDate=2025-02-10&contractId=sec-o-9a4ddcc4778043258ddd4f6de531d0dd' \
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
  --data-raw $'{"operationName":"FetchSecurity","variables":{"securityId":"sec-o-9a4ddcc4778043258ddd4f6de531d0dd"},"query":"query FetchSecurity($securityId: ID\u0021) {\\n  security(id: $securityId) {\\n    ...Security\\n    __typename\\n  }\\n}\\n\\nfragment Blockchain on CryptoBlockchain {\\n  id\\n  networkName\\n  __typename\\n}\\n\\nfragment BlockchainAsset on CryptoBlockchainAsset {\\n  id\\n  blockchain {\\n    ...Blockchain\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment Fundamentals on Fundamentals {\\n  avgVolume\\n  beta\\n  companyCash\\n  companyCeo\\n  companyDebt\\n  companyEarningsGrowth\\n  companyGrossProfitMargin\\n  companyHqLocation\\n  companyRevenue\\n  currency\\n  description\\n  eps\\n  high52Week\\n  inceptionYear\\n  low52Week\\n  marketCap\\n  numberOfEmployees\\n  peRatio\\n  totalAssets\\n  yield\\n  __typename\\n}\\n\\nfragment OptionGreekSymbols on OptionGreekSymbols {\\n  id\\n  rho\\n  vega\\n  delta\\n  theta\\n  gamma\\n  impliedVolatility\\n  calculationTime\\n  __typename\\n}\\n\\nfragment OptionUnderlyingSecurity on Security {\\n  id\\n  currency\\n  status\\n  stock {\\n    name\\n    symbol\\n    primaryMic\\n    primaryExchange\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment ExtendedHoursQuote on ExtendedHoursQuoteDetails {\\n  ask\\n  askAt\\n  askSize\\n  bid\\n  bidAt\\n  bidSize\\n  last\\n  quotedAt\\n  __typename\\n}\\n\\nfragment OptionQuote on QuoteOptionDetails {\\n  openInterest\\n  underlyingSpot\\n  inTheMoney\\n  liquidityStatuses\\n  __typename\\n}\\n\\nfragment SecurityQuote on Quote {\\n  amount\\n  ask\\n  askSize\\n  bid\\n  bidSize\\n  currency\\n  high\\n  last\\n  lastSize\\n  low\\n  open\\n  previousBaseline\\n  previousClosedAt\\n  quotedAsOf\\n  quoteDate\\n  securityId\\n  volume\\n  extendedHoursQuote {\\n    ...ExtendedHoursQuote\\n    __typename\\n  }\\n  optionQuote: quoteOptionDetails {\\n    ...OptionQuote\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment SecurityGroup on PartialSecurityGroup {\\n  id\\n  name\\n  __typename\\n}\\n\\nfragment Stock on Stock {\\n  description\\n  ipoState\\n  name\\n  primaryExchange\\n  primaryMic\\n  segmentMic\\n  symbol\\n  usPtp\\n  __typename\\n}\\n\\nfragment ClientMarginRates on MarginRates {\\n  clientMarginRate\\n  __typename\\n}\\n\\nfragment Security on Security {\\n  active\\n  activeDate\\n  allowedOrderSubtypes\\n  blockchainAssets {\\n    ...BlockchainAsset\\n    __typename\\n  }\\n  buyable\\n  currency\\n  depositEligible\\n  features\\n  fundamentals {\\n    ...Fundamentals\\n    __typename\\n  }\\n  optionDetails {\\n    greekSymbols {\\n      ...OptionGreekSymbols\\n      __typename\\n    }\\n    underlyingSecurity {\\n      ...OptionUnderlyingSecurity\\n      __typename\\n    }\\n    expiryDate\\n    maturity\\n    multiplier\\n    optionType\\n    osiSymbol\\n    strikePrice\\n    __typename\\n  }\\n  id\\n  inactiveDate\\n  isVolatile\\n  marginRates {\\n    ...ClientMarginRates\\n    __typename\\n  }\\n  minWithdrawalAmount\\n  minWalletBalance\\n  quote {\\n    ...SecurityQuote\\n    __typename\\n  }\\n  securityType\\n  securityGroups {\\n    ...SecurityGroup\\n    __typename\\n  }\\n  sellable\\n  settleable\\n  stakeable\\n  status\\n  stock {\\n    ...Stock\\n    __typename\\n  }\\n  tagBased\\n  withdrawEligible\\n  wsTradeEligible\\n  wsTradeIneligibilityReason\\n  optionsEligible\\n  equityTradingSessionType\\n  __typename\\n}"}'

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
    '_oauth2_access_v2': '%7B%22access_token%22%3A%22eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJpZGVudGl0eS1tbEoydE5DdmtHM0IzTzM2emk2MnNMME9ET1UiLCJleHAiOjE3MzkwNTMyMjEsImlhdCI6MTczOTA1MTQyMSwianRpIjoiQ2R4ZDM2M2dTSHNZQXFibHdOZmdDdllnLWVRVTY5VWNTMVRfVzd5RGtHRSIsImNsaWVudF9pZCI6IjRkYTUzYWMyYjAzMjI1YmVkMTU1MGViYThlNDYxMWUwODZjN2I5MDVhMzg1NWU2ZWQxMmVhMDhjMjQ2NzU4ZmEiLCJzY29wZSI6ImludmVzdC5yZWFkIGludmVzdC53cml0ZSB0cmFkZS5yZWFkIHRyYWRlLndyaXRlIHRheC5yZWFkIHRheC53cml0ZSJ9.flsSuG29bJ-EGLO5R-EmAmwrQbONMpeMV4EF1zw6n2FDVc7wUPRnq87OE8lsktelwk7EG82HTMLpCA4frgX8QaGyc48O-Wdl-Q6C3EkkR8RtluvykSBverCnPdHyF3K-uVbmWAGC8rPqLiNL-R9Z3_1cFwrKss6u5qQnyUUbUD7ldutHbgHSPIVpQ1W51UbPs8XcnhJfIeTCQd0o89KQshykCZp8Q0YLxh1s5CgX1zgEFNhPjkzuweYWmUE2-fTg1W-9xYykqB53xXeVCGxSiWbU28r3gRtO4U6eEAS4II8r4Hsd9Ihy43_ZVvKRWSaw0ITgrTQaKfT0Q7t8mqh84g%22%2C%22token_type%22%3A%22Bearer%22%2C%22expires_in%22%3A1800%2C%22refresh_token%22%3A%22kdXhbhmTaD82z2q69yO8zgWJ5nsKsnMYMPAIIHyh1zA%22%2C%22scope%22%3A%22invest.read%20invest.write%20trade.read%20trade.write%20tax.read%20tax.write%22%2C%22created_at%22%3A1739051421%2C%22okta_group_claims%22%3A%5B%5D%2C%22identity_canonical_id%22%3A%22identity-mlJ2tNCvkG3B3O36zi62sL0ODOU%22%2C%22clock_skew%22%3A%7B%22skewed%22%3Afalse%7D%2C%22expires_at%22%3A%222025-02-08T22%3A20%3A21.000Z%22%2C%22email%22%3A%22ahsueh1996%40gmail.com%22%2C%22profiles%22%3A%7B%22tax%22%3A%7B%22default%22%3A%22user-eedww24xbft%22%7D%2C%22trade%22%3A%7B%22default%22%3A%22user-ejs4xw9bbkg%22%7D%2C%22invest%22%3A%7B%22default%22%3A%22user-r2bl3nnqhso%22%7D%7D%2C%22client_canonical_ids%22%3A%7B%22tax%22%3A%7B%22default%22%3A%22person-bdiuyqifzp6yeg%22%7D%2C%22trade%22%3A%7B%22default%22%3A%22person-dnvo5jjaio1pfq%22%7D%2C%22invest%22%3A%7B%22default%22%3A%22person-1p_oiha5naqupq%22%7D%7D%2C%22suspended_profiles%22%3A%7B%7D%7D',
    '_session_id': '84b58b713a44aa80454afc67ff69f5fd',
    'ab.storage.deviceId.80ec85f3-36f6-4cc8-8401-81fb1619363d': 'g%3A6e824410-75e3-b1cb-770b-22d8f3c7b3e2%7Ce%3Aundefined%7Cc%3A1729882007159%7Cl%3A1739051424752',
    'ab.storage.userId.80ec85f3-36f6-4cc8-8401-81fb1619363d': 'g%3Aidentity-mlJ2tNCvkG3B3O36zi62sL0ODOU%7Ce%3Aundefined%7Cc%3A1729882007157%7Cl%3A1739051424753',
    'ab.storage.sessionId.80ec85f3-36f6-4cc8-8401-81fb1619363d': 'g%3Ab5c29665-6202-a2f9-bb63-66d9c3d5c035%7Ce%3A1739051725605%7Cc%3A1739051424751%7Cl%3A1739051425605',
    '_cfuvid': 'O5FwToeg47wcW9XAjsGk5BfsL6FMvYTZ8cegllP2zA4-1739051456976-0.0.1.1-604800000',
    '_dd_s': 'rum=0&expire=1739052360067',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7,zh-CN;q=0.6,ko;q=0.5',
    'authorization': 'Bearer eyJhbGciOiJSU....mlhdCI6MTczOTA1MTQyMSwianRpIjoiQ2R4ZDM2M2dTSH......udF9pZCI6IjRkYTUzYWMyYjAzMjI1......iLCJzY29wZSI6I.........0YLxh1s5CgX1zgEFNhPjkzuweYWmUE2-fTg1W-9xYykqB53xXeVCGxSiWbU28r3gRtO4U6eEAS4II8r4Hsd9Ihy43_ZVvKRWSaw0ITgrTQaKfT0Q7t8mqh84g',
    'content-type': 'application/json',
    'origin': 'https://my.wealthsimple.com',
    'priority': 'u=1, i',
    'referer': 'https://my.wealthsimple.com/app/security-details/sec-s-27167ecbd81140fe9cdc02535f43174d?tab=option_chain&optionType=CALL&expiryDate=2025-02-10&contractId=sec-o-9a4ddcc4778043258ddd4f6de531d0dd',
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
    # 'cookie': 'IR_PI=7ac23cbe-1de5-11ee-8f81-650fe93bdcef%7C1713325456643; lang=en; __stripe_mid=042a30ea-8114-4764-8ca9-d5d9de59deb5036ccb; st_profile=8984583b-4dc9-4bcd-b34e-01e7d9668986; wst_luty=2023; session=.eJxljsEOgjAQBX_F7FVMaEukmHAgGrzqFxC63RIiUlMK1RD-3d48eJ43L7MCTs403j5ohBNIYlpLdUwZzwuUhgTKFDOmuUBVMCMYodJKQQI4O0ejb1pEO48-yvNE7kCkQ-DZWxn_P2p6DScuZC7T7Adf7TQF6yJaYafiUS2v1flZXZZQjbVdhs-wb2_3soQtgcF2Hemmj7XezbR9Af2tQE0.ZnnaxA.HFo_QgTIpJBRkJ5hIUnYTLKkXGs; ws_referrer_url=https://www.google.com/; ws_global_visitor_id=user_be27233bdbbd5d9cd21336ca58316316; wssdi=be27233bdbbd5d9cd21336ca58316316; ws_jurisdiction=CA; __cfruid=ab12f2914664edb63a656dcb18cf4c81f849885c-1730088880; _gcl_au=1.1.597370025.1733040259; _tt_enable_cookie=1; _ttp=2DSc5RSZH-8wmM8rALKCtdpVxvq.tt.1; IR_gbd=wealthsimple.com; _scid=n51vo54Z4XEyOmoQXQ8ampGiKy4shuOY; _sctr=1%7C1733029200000; ajs_user_id=user-r2bl3nnqhso; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2FPekbol7rMROh4Ketr4PuNz4uozog0iXE%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2Bm3H3HlqH8mvBpy7sFzRiESiTlG1g3G6Ka%2F%2FKsmGe%2By%2FJd7fskM2Trf%2FpXb8sKCbCOshzrZQPQ6Q%3D%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX1%2BQvXZ8n0ZJY8pRjPs5mcGXBwRmwPh2U3g%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX18wPQ3QXmJTUDgNrRLEkhML4scS9Tdmj9Q%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2B5QMk1uSRvdzEIIirnca45ZDfFAtcFNOg%3D; _gcl_aw=GCL.1733268910.CjwKCAiA9bq6BhAKEiwAH6bqoF5QvXLWsp76wwZL2S-Le_G4iKfod4Nz708jY0QjRcPwzkMoilzqsBoCa5IQAvD_BwE; _gcl_gs=2.1.k1$i1733268909$u183234660; _ga=GA1.1.561341326.1733040259; tatari-session-cookie=bff4bb99-0b59-c124-66b6-c6d46a9b18a5; _scid_r=rx1vo54Z4XEyOmoQXQ8ampGiKy4shuOYGPcn0A; _rdt_uuid=1733040259224.769f2a82-c0d4-452e-aa5f-7f2f3f105c4c; _ga_P3KV5N62JS=GS1.1.1733435040.5.0.1733435043.57.0.0; ajs_anonymous_id=164f2556-8f13-4ede-9802-432987a6d391; IR_5571=1733435047906%7C0%7C1733435047906%7C%7C; _oauth2_access_v2=%7B%22access_token%22%3A%22eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJpZGVudGl0eS1tbEoydE5DdmtHM0IzTzM2emk2MnNMME9ET1UiLCJleHAiOjE3MzkwNTMyMjEsImlhdCI6MTczOTA1MTQyMSwianRpIjoiQ2R4ZDM2M2dTSHNZQXFibHdOZmdDdllnLWVRVTY5VWNTMVRfVzd5RGtHRSIsImNsaWVudF9pZCI6IjRkYTUzYWMyYjAzMjI1YmVkMTU1MGViYThlNDYxMWUwODZjN2I5MDVhMzg1NWU2ZWQxMmVhMDhjMjQ2NzU4ZmEiLCJzY29wZSI6ImludmVzdC5yZWFkIGludmVzdC53cml0ZSB0cmFkZS5yZWFkIHRyYWRlLndyaXRlIHRheC5yZWFkIHRheC53cml0ZSJ9.flsSuG29bJ-EGLO5R-EmAmwrQbONMpeMV4EF1zw6n2FDVc7wUPRnq87OE8lsktelwk7EG82HTMLpCA4frgX8QaGyc48O-Wdl-Q6C3EkkR8RtluvykSBverCnPdHyF3K-uVbmWAGC8rPqLiNL-R9Z3_1cFwrKss6u5qQnyUUbUD7ldutHbgHSPIVpQ1W51UbPs8XcnhJfIeTCQd0o89KQshykCZp8Q0YLxh1s5CgX1zgEFNhPjkzuweYWmUE2-fTg1W-9xYykqB53xXeVCGxSiWbU28r3gRtO4U6eEAS4II8r4Hsd9Ihy43_ZVvKRWSaw0ITgrTQaKfT0Q7t8mqh84g%22%2C%22token_type%22%3A%22Bearer%22%2C%22expires_in%22%3A1800%2C%22refresh_token%22%3A%22kdXhbhmTaD82z2q69yO8zgWJ5nsKsnMYMPAIIHyh1zA%22%2C%22scope%22%3A%22invest.read%20invest.write%20trade.read%20trade.write%20tax.read%20tax.write%22%2C%22created_at%22%3A1739051421%2C%22okta_group_claims%22%3A%5B%5D%2C%22identity_canonical_id%22%3A%22identity-mlJ2tNCvkG3B3O36zi62sL0ODOU%22%2C%22clock_skew%22%3A%7B%22skewed%22%3Afalse%7D%2C%22expires_at%22%3A%222025-02-08T22%3A20%3A21.000Z%22%2C%22email%22%3A%22ahsueh1996%40gmail.com%22%2C%22profiles%22%3A%7B%22tax%22%3A%7B%22default%22%3A%22user-eedww24xbft%22%7D%2C%22trade%22%3A%7B%22default%22%3A%22user-ejs4xw9bbkg%22%7D%2C%22invest%22%3A%7B%22default%22%3A%22user-r2bl3nnqhso%22%7D%7D%2C%22client_canonical_ids%22%3A%7B%22tax%22%3A%7B%22default%22%3A%22person-bdiuyqifzp6yeg%22%7D%2C%22trade%22%3A%7B%22default%22%3A%22person-dnvo5jjaio1pfq%22%7D%2C%22invest%22%3A%7B%22default%22%3A%22person-1p_oiha5naqupq%22%7D%7D%2C%22suspended_profiles%22%3A%7B%7D%7D; _session_id=84b58b713a44aa80454afc67ff69f5fd; ab.storage.deviceId.80ec85f3-36f6-4cc8-8401-81fb1619363d=g%3A6e824410-75e3-b1cb-770b-22d8f3c7b3e2%7Ce%3Aundefined%7Cc%3A1729882007159%7Cl%3A1739051424752; ab.storage.userId.80ec85f3-36f6-4cc8-8401-81fb1619363d=g%3Aidentity-mlJ2tNCvkG3B3O36zi62sL0ODOU%7Ce%3Aundefined%7Cc%3A1729882007157%7Cl%3A1739051424753; ab.storage.sessionId.80ec85f3-36f6-4cc8-8401-81fb1619363d=g%3Ab5c29665-6202-a2f9-bb63-66d9c3d5c035%7Ce%3A1739051725605%7Cc%3A1739051424751%7Cl%3A1739051425605; _cfuvid=O5FwToeg47wcW9XAjsGk5BfsL6FMvYTZ8cegllP2zA4-1739051456976-0.0.1.1-604800000; _dd_s=rum=0&expire=1739052360067',
}

json_data = {
    'operationName': 'FetchSecurity',
    'variables': {
        'securityId': 'sec-o-9a4ddcc4778043258ddd4f6de531d0dd',
    },
    'query': 'query FetchSecurity($securityId: ID!) {\n  security(id: $securityId) {\n    ...Security\n    __typename\n  }\n}\n\nfragment Blockchain on CryptoBlockchain {\n  id\n  networkName\n  __typename\n}\n\nfragment BlockchainAsset on CryptoBlockchainAsset {\n  id\n  blockchain {\n    ...Blockchain\n    __typename\n  }\n  __typename\n}\n\nfragment Fundamentals on Fundamentals {\n  avgVolume\n  beta\n  companyCash\n  companyCeo\n  companyDebt\n  companyEarningsGrowth\n  companyGrossProfitMargin\n  companyHqLocation\n  companyRevenue\n  currency\n  description\n  eps\n  high52Week\n  inceptionYear\n  low52Week\n  marketCap\n  numberOfEmployees\n  peRatio\n  totalAssets\n  yield\n  __typename\n}\n\nfragment OptionGreekSymbols on OptionGreekSymbols {\n  id\n  rho\n  vega\n  delta\n  theta\n  gamma\n  impliedVolatility\n  calculationTime\n  __typename\n}\n\nfragment OptionUnderlyingSecurity on Security {\n  id\n  currency\n  status\n  stock {\n    name\n    symbol\n    primaryMic\n    primaryExchange\n    __typename\n  }\n  __typename\n}\n\nfragment ExtendedHoursQuote on ExtendedHoursQuoteDetails {\n  ask\n  askAt\n  askSize\n  bid\n  bidAt\n  bidSize\n  last\n  quotedAt\n  __typename\n}\n\nfragment OptionQuote on QuoteOptionDetails {\n  openInterest\n  underlyingSpot\n  inTheMoney\n  liquidityStatuses\n  __typename\n}\n\nfragment SecurityQuote on Quote {\n  amount\n  ask\n  askSize\n  bid\n  bidSize\n  currency\n  high\n  last\n  lastSize\n  low\n  open\n  previousBaseline\n  previousClosedAt\n  quotedAsOf\n  quoteDate\n  securityId\n  volume\n  extendedHoursQuote {\n    ...ExtendedHoursQuote\n    __typename\n  }\n  optionQuote: quoteOptionDetails {\n    ...OptionQuote\n    __typename\n  }\n  __typename\n}\n\nfragment SecurityGroup on PartialSecurityGroup {\n  id\n  name\n  __typename\n}\n\nfragment Stock on Stock {\n  description\n  ipoState\n  name\n  primaryExchange\n  primaryMic\n  segmentMic\n  symbol\n  usPtp\n  __typename\n}\n\nfragment ClientMarginRates on MarginRates {\n  clientMarginRate\n  __typename\n}\n\nfragment Security on Security {\n  active\n  activeDate\n  allowedOrderSubtypes\n  blockchainAssets {\n    ...BlockchainAsset\n    __typename\n  }\n  buyable\n  currency\n  depositEligible\n  features\n  fundamentals {\n    ...Fundamentals\n    __typename\n  }\n  optionDetails {\n    greekSymbols {\n      ...OptionGreekSymbols\n      __typename\n    }\n    underlyingSecurity {\n      ...OptionUnderlyingSecurity\n      __typename\n    }\n    expiryDate\n    maturity\n    multiplier\n    optionType\n    osiSymbol\n    strikePrice\n    __typename\n  }\n  id\n  inactiveDate\n  isVolatile\n  marginRates {\n    ...ClientMarginRates\n    __typename\n  }\n  minWithdrawalAmount\n  minWalletBalance\n  quote {\n    ...SecurityQuote\n    __typename\n  }\n  securityType\n  securityGroups {\n    ...SecurityGroup\n    __typename\n  }\n  sellable\n  settleable\n  stakeable\n  status\n  stock {\n    ...Stock\n    __typename\n  }\n  tagBased\n  withdrawEligible\n  wsTradeEligible\n  wsTradeIneligibilityReason\n  optionsEligible\n  equityTradingSessionType\n  __typename\n}',
}

response = requests.post('https://my.wealthsimple.com/graphql', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"operationName":"FetchSecurity","variables":{"securityId":"sec-o-9a4ddcc4778043258ddd4f6de531d0dd"},"query":"query FetchSecurity($securityId: ID!) {\\n  security(id: $securityId) {\\n    ...Security\\n    __typename\\n  }\\n}\\n\\nfragment Blockchain on CryptoBlockchain {\\n  id\\n  networkName\\n  __typename\\n}\\n\\nfragment BlockchainAsset on CryptoBlockchainAsset {\\n  id\\n  blockchain {\\n    ...Blockchain\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment Fundamentals on Fundamentals {\\n  avgVolume\\n  beta\\n  companyCash\\n  companyCeo\\n  companyDebt\\n  companyEarningsGrowth\\n  companyGrossProfitMargin\\n  companyHqLocation\\n  companyRevenue\\n  currency\\n  description\\n  eps\\n  high52Week\\n  inceptionYear\\n  low52Week\\n  marketCap\\n  numberOfEmployees\\n  peRatio\\n  totalAssets\\n  yield\\n  __typename\\n}\\n\\nfragment OptionGreekSymbols on OptionGreekSymbols {\\n  id\\n  rho\\n  vega\\n  delta\\n  theta\\n  gamma\\n  impliedVolatility\\n  calculationTime\\n  __typename\\n}\\n\\nfragment OptionUnderlyingSecurity on Security {\\n  id\\n  currency\\n  status\\n  stock {\\n    name\\n    symbol\\n    primaryMic\\n    primaryExchange\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment ExtendedHoursQuote on ExtendedHoursQuoteDetails {\\n  ask\\n  askAt\\n  askSize\\n  bid\\n  bidAt\\n  bidSize\\n  last\\n  quotedAt\\n  __typename\\n}\\n\\nfragment OptionQuote on QuoteOptionDetails {\\n  openInterest\\n  underlyingSpot\\n  inTheMoney\\n  liquidityStatuses\\n  __typename\\n}\\n\\nfragment SecurityQuote on Quote {\\n  amount\\n  ask\\n  askSize\\n  bid\\n  bidSize\\n  currency\\n  high\\n  last\\n  lastSize\\n  low\\n  open\\n  previousBaseline\\n  previousClosedAt\\n  quotedAsOf\\n  quoteDate\\n  securityId\\n  volume\\n  extendedHoursQuote {\\n    ...ExtendedHoursQuote\\n    __typename\\n  }\\n  optionQuote: quoteOptionDetails {\\n    ...OptionQuote\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment SecurityGroup on PartialSecurityGroup {\\n  id\\n  name\\n  __typename\\n}\\n\\nfragment Stock on Stock {\\n  description\\n  ipoState\\n  name\\n  primaryExchange\\n  primaryMic\\n  segmentMic\\n  symbol\\n  usPtp\\n  __typename\\n}\\n\\nfragment ClientMarginRates on MarginRates {\\n  clientMarginRate\\n  __typename\\n}\\n\\nfragment Security on Security {\\n  active\\n  activeDate\\n  allowedOrderSubtypes\\n  blockchainAssets {\\n    ...BlockchainAsset\\n    __typename\\n  }\\n  buyable\\n  currency\\n  depositEligible\\n  features\\n  fundamentals {\\n    ...Fundamentals\\n    __typename\\n  }\\n  optionDetails {\\n    greekSymbols {\\n      ...OptionGreekSymbols\\n      __typename\\n    }\\n    underlyingSecurity {\\n      ...OptionUnderlyingSecurity\\n      __typename\\n    }\\n    expiryDate\\n    maturity\\n    multiplier\\n    optionType\\n    osiSymbol\\n    strikePrice\\n    __typename\\n  }\\n  id\\n  inactiveDate\\n  isVolatile\\n  marginRates {\\n    ...ClientMarginRates\\n    __typename\\n  }\\n  minWithdrawalAmount\\n  minWalletBalance\\n  quote {\\n    ...SecurityQuote\\n    __typename\\n  }\\n  securityType\\n  securityGroups {\\n    ...SecurityGroup\\n    __typename\\n  }\\n  sellable\\n  settleable\\n  stakeable\\n  status\\n  stock {\\n    ...Stock\\n    __typename\\n  }\\n  tagBased\\n  withdrawEligible\\n  wsTradeEligible\\n  wsTradeIneligibilityReason\\n  optionsEligible\\n  equityTradingSessionType\\n  __typename\\n}"}'
#response = requests.post('https://my.wealthsimple.com/graphql', cookies=cookies, headers=headers, data=data)

import copy
def create_request_json(security_id):
    json_data = copy.deepcopy(json_data)
    json_data['variables']['securityId'] = security_id
    return json_data

""" Example Response: Stock SPY
{
    "data": {
        "security": {
            "active": true,
            "activeDate": "2009-02-24",
            "allowedOrderSubtypes": [
                "MARKET",
                "FRACTIONAL",
                "RECURRING_INVESTMENT",
                "LIMIT",
                "STOP_LIMIT"
            ],
            "blockchainAssets": null,
            "buyable": true,
            "currency": "USD",
            "depositEligible": null,
            "features": [
                "OPTIONS_L2ELIGIBLE",
                "EXTENDED_HOURS_ELIGIBLE"
            ],
            "fundamentals": {
                "avgVolume": 49780297.9,
                "beta": 1.0013,
                "companyCash": null,
                "companyCeo": null,
                "companyDebt": null,
                "companyEarningsGrowth": null,
                "companyGrossProfitMargin": null,
                "companyHqLocation": null,
                "companyRevenue": null,
                "currency": "USD",
                "description": "SPY tracks a market cap-weighted index of US large- and mid-cap stocks selected by the S&P Committee.",
                "eps": null,
                "high52Week": 610.78,
                "inceptionYear": null,
                "low52Week": 490.715,
                "marketCap": 631803.6296,
                "numberOfEmployees": null,
                "peRatio": 28.1734,
                "totalAssets": null,
                "yield": 0.0117,
                "__typename": "Fundamentals"
            },
            "optionDetails": null,
            "id": "sec-s-27167ecbd81140fe9cdc02535f43174d",
            "inactiveDate": null,
            "isVolatile": false,
            "marginRates": {
                "clientMarginRate": 0.3,
                "__typename": "MarginRates"
            },
            "minWithdrawalAmount": null,
            "minWalletBalance": null,
            "quote": {
                "amount": "600.87",
                "ask": "600.79",
                "askSize": 100,
                "bid": "600.76",
                "bidSize": 1000,
                "currency": "USD",
                "high": "608.125",
                "last": "600.87",
                "lastSize": 100,
                "low": "600.05",
                "open": "606.83",
                "previousBaseline": "606.32",
                "previousClosedAt": "2025-02-06T21:00:00.000Z",
                "quotedAsOf": "2025-02-08T22:47:04.993Z",
                "quoteDate": "2025-02-07T20:59:47.000Z",
                "securityId": "sec-s-27167ecbd81140fe9cdc02535f43174d",
                "volume": 14891048,
                "extendedHoursQuote": {
                    "ask": "600.49",
                    "askAt": "2025-02-08T01:00:00.000Z",
                    "askSize": 25,
                    "bid": "600.21",
                    "bidAt": "2025-02-08T01:00:00.000Z",
                    "bidSize": 20,
                    "last": "600.2297",
                    "quotedAt": "2025-02-08T00:59:57.000Z",
                    "__typename": "ExtendedHoursQuoteDetails"
                },
                "optionQuote": null,
                "__typename": "Quote"
            },
            "securityType": "EXCHANGE_TRADED_FUND",
            "securityGroups": [
                {
                    "id": "security-group-007r4MsVyhAW",
                    "name": "Fractional Trading",
                    "__typename": "PartialSecurityGroup"
                },
                {
                    "id": "security-group-00843s3ueEXr",
                    "name": "Options",
                    "__typename": "PartialSecurityGroup"
                },
                {
                    "id": "security-group-008DbtRZPCSC",
                    "name": "Extended hours trading",
                    "__typename": "PartialSecurityGroup"
                },
                {
                    "id": "security-group-c6153b067083",
                    "name": "ETFs",
                    "__typename": "PartialSecurityGroup"
                }
            ],
            "sellable": true,
            "settleable": true,
            "stakeable": null,
            "status": "TRADING",
            "stock": {
                "description": null,
                "ipoState": null,
                "name": "SSGA SPDR S&P 500 ETF",
                "primaryExchange": "NYSE",
                "primaryMic": "XNYS",
                "segmentMic": "ARCX",
                "symbol": "SPY",
                "usPtp": false,
                "__typename": "Stock"
            },
            "tagBased": null,
            "withdrawEligible": null,
            "wsTradeEligible": true,
            "wsTradeIneligibilityReason": null,
            "optionsEligible": true,
            "equityTradingSessionType": "REGULAR",
            "__typename": "Security"
        }
    }
}
"""

""" Example Response: Option SPY 2025-02-10 CALL 605.0000
{
    "data": {
        "security": {
            "active": true,
            "activeDate": "2025-01-27",
            "allowedOrderSubtypes": [
                "MARKET",
                "LIMIT",
                "STOP_LIMIT"
            ],
            "blockchainAssets": null,
            "buyable": true,
            "currency": "USD",
            "depositEligible": null,
            "features": [
                "OPTIONS_L2ELIGIBLE"
            ],
            "fundamentals": null,
            "optionDetails": {
                "greekSymbols": {
                    "id": "sec-o-9a4ddcc4778043258ddd4f6de531d0dd",
                    "rho": "0.0119",
                    "vega": "0.1705",
                    "delta": "0.2432",
                    "theta": "-0.3151",
                    "gamma": "0.0548",
                    "impliedVolatility": "0.1050",
                    "calculationTime": "2025-02-07T21:30:23Z",
                    "__typename": "OptionGreekSymbols"
                },
                "underlyingSecurity": {
                    "id": "sec-s-27167ecbd81140fe9cdc02535f43174d",
                    "currency": "USD",
                    "status": "TRADING",
                    "stock": {
                        "name": "SSGA SPDR S&P 500 ETF",
                        "symbol": "SPY",
                        "primaryMic": "XNYS",
                        "primaryExchange": "NYSE",
                        "__typename": "Stock"
                    },
                    "__typename": "Security"
                },
                "expiryDate": "2025-02-10",
                "maturity": null,
                "multiplier": 100,
                "optionType": "CALL",
                "osiSymbol": "SPY   250210C00605000",
                "strikePrice": "605.0000",
                "__typename": "Option"
            },
            "id": "sec-o-9a4ddcc4778043258ddd4f6de531d0dd",
            "inactiveDate": null,
            "isVolatile": false,
            "marginRates": {
                "clientMarginRate": 1,
                "__typename": "MarginRates"
            },
            "minWithdrawalAmount": null,
            "minWalletBalance": null,
            "quote": {
                "amount": "0.6200",
                "ask": "0.6300",
                "askSize": 220,
                "bid": "0.6100",
                "bidSize": 20,
                "currency": "USD",
                "high": "4.2500",
                "last": "0.6200",
                "lastSize": 1,
                "low": "0.5800",
                "open": "3.3100",
                "previousBaseline": "3.0300",
                "previousClosedAt": "2025-02-06T21:00:00.000Z",
                "quotedAsOf": "2025-02-08T23:05:23.167Z",
                "quoteDate": "2025-02-07T21:14:54.000Z",
                "securityId": "sec-o-9a4ddcc4778043258ddd4f6de531d0dd",
                "volume": 80329,
                "extendedHoursQuote": null,
                "optionQuote": {
                    "openInterest": 3795,
                    "underlyingSpot": "600.77",
                    "inTheMoney": false,
                    "liquidityStatuses": [],
                    "__typename": "QuoteOptionDetails"
                },
                "__typename": "Quote"
            },
            "securityType": "OPTION",
            "securityGroups": [],
            "sellable": true,
            "settleable": true,
            "stakeable": null,
            "status": "TRADING",
            "stock": {
                "description": null,
                "ipoState": null,
                "name": "",
                "primaryExchange": null,
                "primaryMic": null,
                "segmentMic": null,
                "symbol": "SPY",
                "usPtp": null,
                "__typename": "Stock"
            },
            "tagBased": null,
            "withdrawEligible": null,
            "wsTradeEligible": true,
            "wsTradeIneligibilityReason": null,
            "optionsEligible": false,
            "equityTradingSessionType": "INDEX_ETF_OPTION",
            "__typename": "Security"
        }
    }
}
"""