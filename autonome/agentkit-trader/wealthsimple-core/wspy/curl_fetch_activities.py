"""
Goto the website and paste the curl command below to convert to python requests
**********************************************************************************************************************************
***** Remember to protect your privacy and remove any sensitive information before pasting the curl command to the website *******
************************************************ https://curlconverter.com/ ******************************************************

curl 'https://my.wealthsimple.com/graphql' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'authorization: Bearer eyJhGc....xJVyigXaiLdPu_bskGhpnMUpvsEUhvQE97vdrkQWqSGYhsWLvcR5rXSEnqNWCOO....8USbbkSORQ9YY1GXBr7hNZWYrlF6VJWcAROcTV6XOUATr6PiI_...7PasVC2S8IdfwISCXgV0i2Cj5gNdw' \
  -H 'content-type: application/json' \
  -H 'cookie: ws_global_visitor_id=5f51a681-3c43-4db9-9342-ed24798724c0; _tt_enable_cookie=1; IR_gbd=wealthsimple.com; wssdi=41521b683939e86c668e7b34745c8461; ajs_user_id=user-r2bl3nnqhso; _ttp=ENEQvi1xSYojKm8TnqLykO1CCs0.tt.1; _cfuvid=N2itggAkvLojQXcSHSMq.6czzTsnSIBcgN4xDefRWRw-1735929829001-0.0.1.1-604800000; ws_global_visitor_id=2f6df067-a378-44d7-a510-d0a63bf4a3c9; ajs_anonymous_id=aea41d51-0363-4b63-84e9-8157535b9335; _oauth2_access_v2=%7B%22access_token%22%3A%22eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJpZGVudGl0eS1tbEoydE5DdmtHM0IzTzM2emk2MnNMME9ET1UiLCJleHAiOjE3MzU5NjAwNjYsImlhdCI6MTczNTk1ODI2NiwianRpIjoiLW1ITkhmN2hITGhwU2hNd0NPQlB1Y1NGd09lUUVjYnFNcjFvUTdmbGJVWSIsImNsaWVudF9pZCI6IjRkYTUzYWMyYjAzMjI1YmVkMTU1MGViYThlNDYxMWUwODZjN2I5MDVhMzg1NWU2ZWQxMmVhMDhjMjQ2NzU4ZmEiLCJzY29wZSI6ImludmVzdC5yZWFkIGludmVzdC53cml0ZSB0cmFkZS5yZWFkIHRyYWRlLndyaXRlIHRheC5yZWFkIHRheC53cml0ZSJ9.2Yf11r2OTtCBNwLQ3yGaGq4WfxJVyigXaiLkP0EJj-tzeRqrw9303r0RGS3OQ55J2e1_QAeA6rv1tnispCG_uzcDVvpbTFXZblTbFhWdPu_bskGhpnMUpvsEUhvQE97vdrkQWqSGZ_oaSdad-g7juY_rMhITzVO4QFYD_YhsWLvcR5rXSEnqNWCOOD4RwXjNPZ2PRYyqPYnfsHQPab3oSI56eDC2D48wW4u8USbbkSORQ9YY1GXBr7hNZWYrlF6VJWcAROcTV6XOUATr6PiI_77AcbN-qSW7TJSAwt-LMmEk6FH7NcmhI3e0Y7PasVC2S8IdfwISCXgV0i2Cj5gNdw%22%2C%22token_type%22%3A%22Bearer%22%2C%22expires_in%22%3A1800%2C%22refresh_token%22%3A%22IHQUZhAKxnhE24e3JQ088agXkhuhtrSuN8u2NmCvHJc%22%2C%22scope%22%3A%22invest.read%20invest.write%20trade.read%20trade.write%20tax.read%20tax.write%22%2C%22created_at%22%3A1735958266%2C%22okta_group_claims%22%3A%5B%5D%2C%22identity_canonical_id%22%3A%22identity-mlJ2tNCvkG3B3O36zi62sL0ODOU%22%2C%22clock_skew%22%3A%7B%22skewed%22%3Afalse%7D%2C%22expires_at%22%3A%222025-01-04T03%3A07%3A46.000Z%22%2C%22email%22%3A%22ahsueh1996%40gmail.com%22%2C%22profiles%22%3A%7B%22tax%22%3A%7B%22default%22%3A%22user-eedww24xbft%22%7D%2C%22trade%22%3A%7B%22default%22%3A%22user-ejs4xw9bbkg%22%7D%2C%22invest%22%3A%7B%22default%22%3A%22user-r2bl3nnqhso%22%7D%7D%2C%22client_canonical_ids%22%3A%7B%22tax%22%3A%7B%22default%22%3A%22person-bdiuyqifzp6yeg%22%7D%2C%22trade%22%3A%7B%22default%22%3A%22person-dnvo5jjaio1pfq%22%7D%2C%22invest%22%3A%7B%22default%22%3A%22person-1p_oiha5naqupq%22%7D%7D%2C%22suspended_profiles%22%3A%7B%7D%7D; ab.storage.deviceId.80ec85f3-36f6-4cc8-8401-81fb1619363d=g%3A26157de1-4856-dbfa-e484-f715e455a091%7Ce%3Aundefined%7Cc%3A1734911250207%7Cl%3A1735959254382; ab.storage.userId.80ec85f3-36f6-4cc8-8401-81fb1619363d=g%3Aidentity-mlJ2tNCvkG3B3O36zi62sL0ODOU%7Ce%3Aundefined%7Cc%3A1734911250205%7Cl%3A1735959254382; ab.storage.sessionId.80ec85f3-36f6-4cc8-8401-81fb1619363d=g%3A2761c71c-db4a-8b55-ef77-8e2619f4b25b%7Ce%3A1735959563529%7Cc%3A1735959254381%7Cl%3A1735959263529; _dd_s=rum=0&expire=1735960255837; IR_5571=1735959356199%7C0%7C1735959356199%7C%7C' \
  -H 'origin: https://my.wealthsimple.com' \
  -H 'priority: u=1, i' \
  -H 'referer: https://my.wealthsimple.com/app/activity?types=dividends,buys,sells,tax,bonus,deposits,interest,fee,fundsConverted,grants,optionsExpired,optionsExercised,cashSentReceived,refundsAndReimbursements,stakingRewards,stakingActions,purchases,transfer,writeOff,withdrawals&security_ids=sec-s-bb0c7dd14c66459c90c01e99a106dbfe,sec-s-27167ecbd81140fe9cdc02535f43174d&status=actionRequired,cancelled,cancelling,completed,declined,expired,failed,inProgress,pending,refunded,rejected,reversed,transferring' \
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
  --data-raw $'{"operationName":"FetchActivityFeedItems","variables":{"orderBy":"OCCURRED_AT_DESC","condition":{"accountIds":["non-registered-qg0kaqvs","non-registered-OIzSXMKX6w","tfsa-efxbb3dd","tfsa-V1SACdWcJA","ca-cash-msb-tTRdeOlyiQ","non-registered-4Abwfg0v8g","non-registered-CVT-UTQOag","tfsa-ZGIkkYSEHw","non-registered-crypto-HCgcCoASuA"],"types":["DIVIDEND","STOCK_DIVIDEND","MANAGED_BUY","CRYPTO_BUY","DIY_BUY","OPTIONS_BUY","MANAGED_SELL","CRYPTO_SELL","DIY_SELL","OPTIONS_SELL","WITHHOLDING_TAX","NON_RESIDENT_TAX","AFFILIATE","PROMOTION","REFERRAL","DEPOSIT","GROUP_CONTRIBUTION","INTEREST","FEE","FUNDS_CONVERSION","RESP_GRANT","OPTIONS_EXPIRY","OPTIONS_EXERCISE","P2P_PAYMENT","REFUND","REIMBURSEMENT","CRYPTO_STAKING_REWARD","CRYPTO_STAKING_ACTION","SPEND","PREPAID_SPEND","CREDIT_CARD","INTERNAL_TRANSFER","INSTITUTIONAL_TRANSFER_INTENT","LEGACY_INTERNAL_TRANSFER","LEGACY_TRANSFER","CRYPTO_TRANSFER","WRITE_OFF","WITHDRAWAL"],"subTypes":["PREPAID","PURCHASE","REFUND","CASH_ADVANCE"],"securityIds":["sec-s-bb0c7dd14c66459c90c01e99a106dbfe","sec-s-27167ecbd81140fe9cdc02535f43174d"],"unifiedStatuses":["ACTION_REQUIRED","CANCELLED","CANCEL_PENDING","COMPLETED","DECLINED","EXPIRED","FAILED","IN_PROGRESS","PENDING","REFUNDED","REJECTED","REVERSED","TRANSFERRING"],"endDate":"2025-01-04T04:59:59.999Z"},"first":50},"query":"query FetchActivityFeedItems($first: Int, $cursor: Cursor, $condition: ActivityCondition, $orderBy: [ActivitiesOrderBy\u0021] = OCCURRED_AT_DESC) {\\n  activityFeedItems(\\n    first: $first\\n    after: $cursor\\n    condition: $condition\\n    orderBy: $orderBy\\n  ) {\\n    edges {\\n      node {\\n        ...Activity\\n        __typename\\n      }\\n      __typename\\n    }\\n    pageInfo {\\n      hasNextPage\\n      endCursor\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n\\nfragment Activity on ActivityFeedItem {\\n  accountId\\n  aftOriginatorName\\n  aftTransactionCategory\\n  aftTransactionType\\n  amount\\n  amountSign\\n  assetQuantity\\n  assetSymbol\\n  canonicalId\\n  currency\\n  eTransferEmail\\n  eTransferName\\n  externalCanonicalId\\n  identityId\\n  institutionName\\n  occurredAt\\n  p2pHandle\\n  p2pMessage\\n  spendMerchant\\n  securityId\\n  billPayCompanyName\\n  billPayPayeeNickname\\n  redactedExternalAccountNumber\\n  opposingAccountId\\n  status\\n  subType\\n  type\\n  strikePrice\\n  contractType\\n  expiryDate\\n  chequeNumber\\n  provisionalCreditAmount\\n  primaryBlocker\\n  interestRate\\n  frequency\\n  counterAssetSymbol\\n  rewardProgram\\n  counterPartyCurrency\\n  counterPartyCurrencyAmount\\n  counterPartyName\\n  fxRate\\n  fees\\n  reference\\n  __typename\\n}"}'

"""

# paste the python code below
import requests

cookies = {
    'ws_global_visitor_id': '5f51a681-3c43-4db9-9342-ed24798724c0',
    '_tt_enable_cookie': '1',
    'IR_gbd': 'wealthsimple.com',
    'wssdi': '41521b683939e86c668e7b34745c8461',
    'ajs_user_id': 'user-r2bl3nnqhso',
    '_ttp': 'ENEQvi1xSYojKm8TnqLykO1CCs0.tt.1',
    '_cfuvid': 'N2itggAkvLojQXcSHSMq.6czzTsnSIBcgN4xDefRWRw-1735929829001-0.0.1.1-604800000',
    'ws_global_visitor_id': '2f6df067-a378-44d7-a510-d0a63bf4a3c9',
    'ajs_anonymous_id': 'aea41d51-0363-4b63-84e9-8157535b9335',
    '_oauth2_access_v2': '%7B%22access_token%22%3A%22eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJpZGVudGl0eS1tbEoydE5DdmtHM0IzTzM2emk2MnNMME9ET1UiLCJleHAiOjE3MzU5NjAwNjYsImlhdCI6MTczNTk1ODI2NiwianRpIjoiLW1ITkhmN2hITGhwU2hNd0NPQlB1Y1NGd09lUUVjYnFNcjFvUTdmbGJVWSIsImNsaWVudF9pZCI6IjRkYTUzYWMyYjAzMjI1YmVkMTU1MGViYThlNDYxMWUwODZjN2I5MDVhMzg1NWU2ZWQxMmVhMDhjMjQ2NzU4ZmEiLCJzY29wZSI6ImludmVzdC5yZWFkIGludmVzdC53cml0ZSB0cmFkZS5yZWFkIHRyYWRlLndyaXRlIHRheC5yZWFkIHRheC53cml0ZSJ9.2Yf11r2OTtCBNwLQ3yGaGq4WfxJVyigXaiLkP0EJj-tzeRqrw9303r0RGS3OQ55J2e1_QAeA6rv1tnispCG_uzcDVvpbTFXZblTbFhWdPu_bskGhpnMUpvsEUhvQE97vdrkQWqSGZ_oaSdad-g7juY_rMhITzVO4QFYD_YhsWLvcR5rXSEnqNWCOOD4RwXjNPZ2PRYyqPYnfsHQPab3oSI56eDC2D48wW4u8USbbkSORQ9YY1GXBr7hNZWYrlF6VJWcAROcTV6XOUATr6PiI_77AcbN-qSW7TJSAwt-LMmEk6FH7NcmhI3e0Y7PasVC2S8IdfwISCXgV0i2Cj5gNdw%22%2C%22token_type%22%3A%22Bearer%22%2C%22expires_in%22%3A1800%2C%22refresh_token%22%3A%22IHQUZhAKxnhE24e3JQ088agXkhuhtrSuN8u2NmCvHJc%22%2C%22scope%22%3A%22invest.read%20invest.write%20trade.read%20trade.write%20tax.read%20tax.write%22%2C%22created_at%22%3A1735958266%2C%22okta_group_claims%22%3A%5B%5D%2C%22identity_canonical_id%22%3A%22identity-mlJ2tNCvkG3B3O36zi62sL0ODOU%22%2C%22clock_skew%22%3A%7B%22skewed%22%3Afalse%7D%2C%22expires_at%22%3A%222025-01-04T03%3A07%3A46.000Z%22%2C%22email%22%3A%22ahsueh1996%40gmail.com%22%2C%22profiles%22%3A%7B%22tax%22%3A%7B%22default%22%3A%22user-eedww24xbft%22%7D%2C%22trade%22%3A%7B%22default%22%3A%22user-ejs4xw9bbkg%22%7D%2C%22invest%22%3A%7B%22default%22%3A%22user-r2bl3nnqhso%22%7D%7D%2C%22client_canonical_ids%22%3A%7B%22tax%22%3A%7B%22default%22%3A%22person-bdiuyqifzp6yeg%22%7D%2C%22trade%22%3A%7B%22default%22%3A%22person-dnvo5jjaio1pfq%22%7D%2C%22invest%22%3A%7B%22default%22%3A%22person-1p_oiha5naqupq%22%7D%7D%2C%22suspended_profiles%22%3A%7B%7D%7D',
    'ab.storage.deviceId.80ec85f3-36f6-4cc8-8401-81fb1619363d': 'g%3A26157de1-4856-dbfa-e484-f715e455a091%7Ce%3Aundefined%7Cc%3A1734911250207%7Cl%3A1735959254382',
    'ab.storage.userId.80ec85f3-36f6-4cc8-8401-81fb1619363d': 'g%3Aidentity-mlJ2tNCvkG3B3O36zi62sL0ODOU%7Ce%3Aundefined%7Cc%3A1734911250205%7Cl%3A1735959254382',
    'ab.storage.sessionId.80ec85f3-36f6-4cc8-8401-81fb1619363d': 'g%3A2761c71c-db4a-8b55-ef77-8e2619f4b25b%7Ce%3A1735959563529%7Cc%3A1735959254381%7Cl%3A1735959263529',
    '_dd_s': 'rum=0&expire=1735960255837',
    'IR_5571': '1735959356199%7C0%7C1735959356199%7C%7C',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer eyJhGciOiJSUzI;;;;;TtCBNwLQ3yGaGq4WfxJVyigXaiLd,,,D4RwXjNPZ2PRYyqPYnfsHQPab3...Y1GXBr7hNZWYrlF6VJWcAROcTV6XOUATr6PiI_77AcbN-qSW7TJSAwt-LMmEk6FH7NcmhI3e0Y7PasVC2S8IdfwISCXgV0i2Cj5gNdw',
    'content-type': 'application/json',
    # 'cookie': 'ws_global_visitor_id=5f51a681-3c43-4db9-9342-ed24798724c0; _tt_enable_cookie=1; IR_gbd=wealthsimple.com; wssdi=41521b683939e86c668e7b34745c8461; ajs_user_id=user-r2bl3nnqhso; _ttp=ENEQvi1xSYojKm8TnqLykO1CCs0.tt.1; _cfuvid=N2itggAkvLojQXcSHSMq.6czzTsnSIBcgN4xDefRWRw-1735929829001-0.0.1.1-604800000; ws_global_visitor_id=2f6df067-a378-44d7-a510-d0a63bf4a3c9; ajs_anonymous_id=aea41d51-0363-4b63-84e9-8157535b9335; _oauth2_access_v2=%7B%22access_token%22%3A%22eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJpZGVudGl0eS1tbEoydE5DdmtHM0IzTzM2emk2MnNMME9ET1UiLCJleHAiOjE3MzU5NjAwNjYsImlhdCI6MTczNTk1ODI2NiwianRpIjoiLW1ITkhmN2hITGhwU2hNd0NPQlB1Y1NGd09lUUVjYnFNcjFvUTdmbGJVWSIsImNsaWVudF9pZCI6IjRkYTUzYWMyYjAzMjI1YmVkMTU1MGViYThlNDYxMWUwODZjN2I5MDVhMzg1NWU2ZWQxMmVhMDhjMjQ2NzU4ZmEiLCJzY29wZSI6ImludmVzdC5yZWFkIGludmVzdC53cml0ZSB0cmFkZS5yZWFkIHRyYWRlLndyaXRlIHRheC5yZWFkIHRheC53cml0ZSJ9.2Yf11r2OTtCBNwLQ3yGaGq4WfxJVyigXaiLkP0EJj-tzeRqrw9303r0RGS3OQ55J2e1_QAeA6rv1tnispCG_uzcDVvpbTFXZblTbFhWdPu_bskGhpnMUpvsEUhvQE97vdrkQWqSGZ_oaSdad-g7juY_rMhITzVO4QFYD_YhsWLvcR5rXSEnqNWCOOD4RwXjNPZ2PRYyqPYnfsHQPab3oSI56eDC2D48wW4u8USbbkSORQ9YY1GXBr7hNZWYrlF6VJWcAROcTV6XOUATr6PiI_77AcbN-qSW7TJSAwt-LMmEk6FH7NcmhI3e0Y7PasVC2S8IdfwISCXgV0i2Cj5gNdw%22%2C%22token_type%22%3A%22Bearer%22%2C%22expires_in%22%3A1800%2C%22refresh_token%22%3A%22IHQUZhAKxnhE24e3JQ088agXkhuhtrSuN8u2NmCvHJc%22%2C%22scope%22%3A%22invest.read%20invest.write%20trade.read%20trade.write%20tax.read%20tax.write%22%2C%22created_at%22%3A1735958266%2C%22okta_group_claims%22%3A%5B%5D%2C%22identity_canonical_id%22%3A%22identity-mlJ2tNCvkG3B3O36zi62sL0ODOU%22%2C%22clock_skew%22%3A%7B%22skewed%22%3Afalse%7D%2C%22expires_at%22%3A%222025-01-04T03%3A07%3A46.000Z%22%2C%22email%22%3A%22ahsueh1996%40gmail.com%22%2C%22profiles%22%3A%7B%22tax%22%3A%7B%22default%22%3A%22user-eedww24xbft%22%7D%2C%22trade%22%3A%7B%22default%22%3A%22user-ejs4xw9bbkg%22%7D%2C%22invest%22%3A%7B%22default%22%3A%22user-r2bl3nnqhso%22%7D%7D%2C%22client_canonical_ids%22%3A%7B%22tax%22%3A%7B%22default%22%3A%22person-bdiuyqifzp6yeg%22%7D%2C%22trade%22%3A%7B%22default%22%3A%22person-dnvo5jjaio1pfq%22%7D%2C%22invest%22%3A%7B%22default%22%3A%22person-1p_oiha5naqupq%22%7D%7D%2C%22suspended_profiles%22%3A%7B%7D%7D; ab.storage.deviceId.80ec85f3-36f6-4cc8-8401-81fb1619363d=g%3A26157de1-4856-dbfa-e484-f715e455a091%7Ce%3Aundefined%7Cc%3A1734911250207%7Cl%3A1735959254382; ab.storage.userId.80ec85f3-36f6-4cc8-8401-81fb1619363d=g%3Aidentity-mlJ2tNCvkG3B3O36zi62sL0ODOU%7Ce%3Aundefined%7Cc%3A1734911250205%7Cl%3A1735959254382; ab.storage.sessionId.80ec85f3-36f6-4cc8-8401-81fb1619363d=g%3A2761c71c-db4a-8b55-ef77-8e2619f4b25b%7Ce%3A1735959563529%7Cc%3A1735959254381%7Cl%3A1735959263529; _dd_s=rum=0&expire=1735960255837; IR_5571=1735959356199%7C0%7C1735959356199%7C%7C',
    'origin': 'https://my.wealthsimple.com',
    'priority': 'u=1, i',
    'referer': 'https://my.wealthsimple.com/app/activity?types=dividends,buys,sells,tax,bonus,deposits,interest,fee,fundsConverted,grants,optionsExpired,optionsExercised,cashSentReceived,refundsAndReimbursements,stakingRewards,stakingActions,purchases,transfer,writeOff,withdrawals&security_ids=sec-s-bb0c7dd14c66459c90c01e99a106dbfe,sec-s-27167ecbd81140fe9cdc02535f43174d&status=actionRequired,cancelled,cancelling,completed,declined,expired,failed,inProgress,pending,refunded,rejected,reversed,transferring',
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
    'operationName': 'FetchActivityFeedItems',
    'variables': {
        'orderBy': 'OCCURRED_AT_DESC',
        'condition': {
            'accountIds': [
                'secret',      # CAD account
                'secret?? is it really.. but at least it is specific to user',    # USD account
            ],
            'types': [
                'DIVIDEND',
                'STOCK_DIVIDEND',
                'MANAGED_BUY',
                'CRYPTO_BUY',
                'DIY_BUY',
                'OPTIONS_BUY',
                'MANAGED_SELL',
                'CRYPTO_SELL',
                'DIY_SELL',
                'OPTIONS_SELL',
                'WITHHOLDING_TAX',
                'NON_RESIDENT_TAX',
                'AFFILIATE',
                'PROMOTION',
                'REFERRAL',
                'DEPOSIT',
                'GROUP_CONTRIBUTION',
                'INTEREST',
                'FEE',
                'FUNDS_CONVERSION',
                'RESP_GRANT',
                'OPTIONS_EXPIRY',
                'OPTIONS_EXERCISE',
                'P2P_PAYMENT',
                'REFUND',
                'REIMBURSEMENT',
                'CRYPTO_STAKING_REWARD',
                'CRYPTO_STAKING_ACTION',
                'SPEND',
                'PREPAID_SPEND',
                'CREDIT_CARD',
                'INTERNAL_TRANSFER',
                'INSTITUTIONAL_TRANSFER_INTENT',
                'LEGACY_INTERNAL_TRANSFER',
                'LEGACY_TRANSFER',
                'CRYPTO_TRANSFER',
                'WRITE_OFF',
                'WITHDRAWAL',
            ],
            'subTypes': [
                'PREPAID',
                'PURCHASE',
                'REFUND',
                'CASH_ADVANCE',
            ],
            'securityIds': [
                'sec-s-bb0c7dd14c66459c90c01e99a106dbfe',
                'sec-s-27167ecbd81140fe9cdc02535f43174d',
            ],
            'unifiedStatuses': [
                'ACTION_REQUIRED',
                'CANCELLED',
                'CANCEL_PENDING',
                'COMPLETED',
                'DECLINED',
                'EXPIRED',
                'FAILED',
                'IN_PROGRESS',
                'PENDING',
                'REFUNDED',
                'REJECTED',
                'REVERSED',
                'TRANSFERRING',
            ],
            'endDate': '2025-01-04T04:59:59.999Z',
        },
        'first': 50,
    },
    'query': 'query FetchActivityFeedItems($first: Int, $cursor: Cursor, $condition: ActivityCondition, $orderBy: [ActivitiesOrderBy!] = OCCURRED_AT_DESC) {\n  activityFeedItems(\n    first: $first\n    after: $cursor\n    condition: $condition\n    orderBy: $orderBy\n  ) {\n    edges {\n      node {\n        ...Activity\n        __typename\n      }\n      __typename\n    }\n    pageInfo {\n      hasNextPage\n      endCursor\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment Activity on ActivityFeedItem {\n  accountId\n  aftOriginatorName\n  aftTransactionCategory\n  aftTransactionType\n  amount\n  amountSign\n  assetQuantity\n  assetSymbol\n  canonicalId\n  currency\n  eTransferEmail\n  eTransferName\n  externalCanonicalId\n  identityId\n  institutionName\n  occurredAt\n  p2pHandle\n  p2pMessage\n  spendMerchant\n  securityId\n  billPayCompanyName\n  billPayPayeeNickname\n  redactedExternalAccountNumber\n  opposingAccountId\n  status\n  subType\n  type\n  strikePrice\n  contractType\n  expiryDate\n  chequeNumber\n  provisionalCreditAmount\n  primaryBlocker\n  interestRate\n  frequency\n  counterAssetSymbol\n  rewardProgram\n  counterPartyCurrency\n  counterPartyCurrencyAmount\n  counterPartyName\n  fxRate\n  fees\n  reference\n  __typename\n}',
}

response = requests.post('https://my.wealthsimple.com/graphql', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"operationName":"FetchActivityFeedItems","variables":{"orderBy":"OCCURRED_AT_DESC","condition":{"accountIds":["non-registered-qg0kaqvs","non-registered-OIzSXMKX6w","tfsa-efxbb3dd","tfsa-V1SACdWcJA","ca-cash-msb-tTRdeOlyiQ","non-registered-4Abwfg0v8g","non-registered-CVT-UTQOag","tfsa-ZGIkkYSEHw","non-registered-crypto-HCgcCoASuA"],"types":["DIVIDEND","STOCK_DIVIDEND","MANAGED_BUY","CRYPTO_BUY","DIY_BUY","OPTIONS_BUY","MANAGED_SELL","CRYPTO_SELL","DIY_SELL","OPTIONS_SELL","WITHHOLDING_TAX","NON_RESIDENT_TAX","AFFILIATE","PROMOTION","REFERRAL","DEPOSIT","GROUP_CONTRIBUTION","INTEREST","FEE","FUNDS_CONVERSION","RESP_GRANT","OPTIONS_EXPIRY","OPTIONS_EXERCISE","P2P_PAYMENT","REFUND","REIMBURSEMENT","CRYPTO_STAKING_REWARD","CRYPTO_STAKING_ACTION","SPEND","PREPAID_SPEND","CREDIT_CARD","INTERNAL_TRANSFER","INSTITUTIONAL_TRANSFER_INTENT","LEGACY_INTERNAL_TRANSFER","LEGACY_TRANSFER","CRYPTO_TRANSFER","WRITE_OFF","WITHDRAWAL"],"subTypes":["PREPAID","PURCHASE","REFUND","CASH_ADVANCE"],"securityIds":["sec-s-bb0c7dd14c66459c90c01e99a106dbfe","sec-s-27167ecbd81140fe9cdc02535f43174d"],"unifiedStatuses":["ACTION_REQUIRED","CANCELLED","CANCEL_PENDING","COMPLETED","DECLINED","EXPIRED","FAILED","IN_PROGRESS","PENDING","REFUNDED","REJECTED","REVERSED","TRANSFERRING"],"endDate":"2025-01-04T04:59:59.999Z"},"first":50},"query":"query FetchActivityFeedItems($first: Int, $cursor: Cursor, $condition: ActivityCondition, $orderBy: [ActivitiesOrderBy!] = OCCURRED_AT_DESC) {\\n  activityFeedItems(\\n    first: $first\\n    after: $cursor\\n    condition: $condition\\n    orderBy: $orderBy\\n  ) {\\n    edges {\\n      node {\\n        ...Activity\\n        __typename\\n      }\\n      __typename\\n    }\\n    pageInfo {\\n      hasNextPage\\n      endCursor\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n\\nfragment Activity on ActivityFeedItem {\\n  accountId\\n  aftOriginatorName\\n  aftTransactionCategory\\n  aftTransactionType\\n  amount\\n  amountSign\\n  assetQuantity\\n  assetSymbol\\n  canonicalId\\n  currency\\n  eTransferEmail\\n  eTransferName\\n  externalCanonicalId\\n  identityId\\n  institutionName\\n  occurredAt\\n  p2pHandle\\n  p2pMessage\\n  spendMerchant\\n  securityId\\n  billPayCompanyName\\n  billPayPayeeNickname\\n  redactedExternalAccountNumber\\n  opposingAccountId\\n  status\\n  subType\\n  type\\n  strikePrice\\n  contractType\\n  expiryDate\\n  chequeNumber\\n  provisionalCreditAmount\\n  primaryBlocker\\n  interestRate\\n  frequency\\n  counterAssetSymbol\\n  rewardProgram\\n  counterPartyCurrency\\n  counterPartyCurrencyAmount\\n  counterPartyName\\n  fxRate\\n  fees\\n  reference\\n  __typename\\n}"}'
#response = requests.post('https://my.wealthsimple.com/graphql', cookies=cookies, headers=headers, data=data)


import copy
from datetime import datetime

def create_default_fetch_activities(accountIds):
    global json_data
    jd = copy.deepcopy(json_data)
    jd['variables']['condition']['accountIds'] = accountIds  # pass all the accounts you want to fetch here
    jd['variables']['condition'].pop('subTypes', None)
    jd['variables']['condition']['endDate'] = datetime.utcnow().isoformat()+"Z"
    jd['variables']['condition'].pop('securityIds', None) # all securities
    jd['variables']['condition']['first'] = 500
    jd['variables']['condition']['unifiedStatuses'] = ['COMPLETED']
    return jd

'''
Sample response.json()

{
    "data": {
        "activityFeedItems": {
            "edges": [
                {
                    "node": {
                        "accountId": "nsecreet",
                        "aftOriginatorName": null,
                        "aftTransactionCategory": null,
                        "aftTransactionType": null,
                        "amount": "93.46",
                        "amountSign": "positive",
                        "assetQuantity": "2.0000",
                        "assetSymbol": "IONQ",
                        "canonicalId": "order-00XcBYy3rzTk",
                        "currency": "USD",
                        "eTransferEmail": null,
                        "eTransferName": null,
                        "externalCanonicalId": "order-6eddcda4-7b6c-43e2-b92b-e857a0cdabff",
                        "identityId": null,
                        "institutionName": null,
                        "occurredAt": "2025-01-03T16:45:51.587000+00:00",
                        "p2pHandle": null,
                        "p2pMessage": null,
                        "spendMerchant": null,
                        "securityId": "sec-s-3d91e20fafb4478b82065e7678866738",
                        "billPayCompanyName": null,
                        "billPayPayeeNickname": null,
                        "redactedExternalAccountNumber": null,
                        "opposingAccountId": null,
                        "status": "FILLED",
                        "subType": "LIMIT_ORDER",
                        "type": "DIY_SELL",
                        "strikePrice": null,
                        "contractType": null,
                        "expiryDate": null,
                        "chequeNumber": null,
                        "provisionalCreditAmount": null,
                        "primaryBlocker": null,
                        "interestRate": null,
                        "frequency": null,
                        "counterAssetSymbol": null,
                        "rewardProgram": null,
                        "counterPartyCurrency": null,
                        "counterPartyCurrencyAmount": null,
                        "counterPartyName": null,
                        "fxRate": null,
                        "fees": null,
                        "reference": null,
                        "__typename": "ActivityFeedItem"
                    },
                    "__typename": "ActivitiesEdge"
                },
            ],
            "pageInfo": {
                "hasNextPage": false,
                "endCursor": "WyIwYTJhOWJjMGNlIiwiMjAyNC0xMi0xOVQxNDozNzozNC44MjEwMDArMDA6MDAiLCJvcmRlci0wMFhhY2FDVUFqUTUiXQ==",
                "__typename": "PageInfo"
            },
            "__typename": "ActivitiesConnection"
        }
    }
}
'''
