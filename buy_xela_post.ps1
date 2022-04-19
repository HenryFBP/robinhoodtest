$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
$session.UserAgent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36"
Invoke-WebRequest -UseBasicParsing -Uri "https://api.robinhood.com/orders/" `
-Method "POST" `
-WebSession $session `
-Headers @{
"authority"="api.robinhood.com"
  "method"="POST"
  "path"="/orders/"
  "scheme"="https"
  "accept"="*/*"
  "accept-encoding"="gzip, deflate, br"
  "accept-language"="en-US,en;q=0.9"
  "authorization"="Bearer coolbeans420"
  "dnt"="1"
  "origin"="https://robinhood.com"
  "referer"="https://robinhood.com/"
  "sec-ch-ua"="`" Not A;Brand`";v=`"99`", `"Chromium`";v=`"100`", `"Google Chrome`";v=`"100`""
  "sec-ch-ua-mobile"="?1"
  "sec-ch-ua-platform"="`"Android`""
  "sec-fetch-dest"="empty"
  "sec-fetch-mode"="cors"
  "sec-fetch-site"="same-site"
} `
-ContentType "application/json" `
-Body "{`"account`":`"https://api.robinhood.com/accounts/furry/`",`"extended_hours`":false,`"instrument`":`"https://api.robinhood.com/instruments/af3ee8c5-5548-4ed0-bb0b-8e1df1cafa8f/`",`"quantity`":`"1`",`"ref_id`":`"58b833bc-276d-473d-923b-ad94b5a687d3`",`"side`":`"buy`",`"symbol`":`"XELA`",`"time_in_force`":`"gfd`",`"trigger`":`"immediate`",`"type`":`"market`",`"price`":`"0.4013`"}"

# and then they respond with... (copied from HAR)

@"
        "response": {
          "status": 201,
          "statusText": "",
          "httpVersion": "http/2.0",
          "headers": [
            {
              "name": "access-control-allow-origin",
              "value": "https://robinhood.com"
            },
            {
              "name": "allow",
              "value": "GET, POST, HEAD, OPTIONS"
            },
            {
              "name": "content-language",
              "value": "en-us"
            },
            {
              "name": "content-length",
              "value": "1748"
            },
            {
              "name": "content-type",
              "value": "application/json"
            },
            {
              "name": "date",
              "value": "Mon, 18 Apr 2022 23:27:42 GMT"
            },
            {
              "name": "location",
              "value": "https://api.robinhood.com/orders/625df3ee-4a7e-4e17-a128-02177bd4b7da/"
            },
            {
              "name": "server",
              "value": "envoy"
            },
            {
              "name": "trace-uuid",
              "value": "62325b49-bfbb-4ab6-b038-bc1d94f713c5"
            },
            {
              "name": "vary",
              "value": "Accept-Language, Cookie, Origin"
            },
            {
              "name": "x-envoy-upstream-service-time",
              "value": "272"
            },
            {
              "name": "x-robinhood-api-version",
              "value": "brokeback/1.433.103-1649893324-gb24b07c130ade86b6b3a1cd19efc172de0091193"
            }
          ],
          "cookies": [],
          "content": {
            "size": 1748,
            "mimeType": "application/json",
            "text": "{\"id\":\"625df3ee-4a7e-4e17-a128-02177bd4b7da\",\"ref_id\":\"58b833bc-276d-473d-923b-ad94b5a687d3\",\"url\":\"https:\\/\\/api.robinhood.com\\/orders\\/625df3ee-4a7e-4e17-a128-02177bd4b7da\\/\",\"account\":\"https:\\/\\/api.robinhood.com\\/accounts\\/furry\\/\",\"position\":\"https:\\/\\/api.robinhood.com\\/positions\\/furry\\/af3ee8c5-5548-4ed0-bb0b-8e1df1cafa8f\\/\",\"cancel\":\"https:\\/\\/api.robinhood.com\\/orders\\/625df3ee-4a7e-4e17-a128-02177bd4b7da\\/cancel\\/\",\"instrument\":\"https:\\/\\/api.robinhood.com\\/instruments\\/af3ee8c5-5548-4ed0-bb0b-8e1df1cafa8f\\/\",\"instrument_id\":\"af3ee8c5-5548-4ed0-bb0b-8e1df1cafa8f\",\"cumulative_quantity\":\"0.00000000\",\"average_price\":null,\"fees\":\"0.00\",\"state\":\"unconfirmed\",\"pending_cancel_open_agent\":null,\"type\":\"market\",\"side\":\"buy\",\"time_in_force\":\"gfd\",\"trigger\":\"immediate\",\"price\":\"0.40130000\",\"stop_price\":null,\"quantity\":\"1.00000000\",\"reject_reason\":null,\"created_at\":\"2022-04-18T23:27:42.622249Z\",\"updated_at\":\"2022-04-18T23:27:42.622270Z\",\"last_transaction_at\":\"2022-04-18T23:27:42.622249Z\",\"executions\":[],\"extended_hours\":false,\"override_dtbp_checks\":false,\"override_day_trade_checks\":false,\"response_category\":null,\"stop_triggered_at\":null,\"last_trail_price\":null,\"last_trail_price_updated_at\":null,\"dollar_based_amount\":null,\"total_notional\":{\"amount\":\"0.41\",\"currency_code\":\"USD\",\"currency_id\":\"1072fc76-1862-41ab-82c2-485837590762\"},\"executed_notional\":null,\"investment_schedule_id\":null,\"is_ipo_access_order\":false,\"ipo_access_cancellation_reason\":null,\"ipo_access_lower_collared_price\":null,\"ipo_access_upper_collared_price\":null,\"ipo_access_upper_price\":null,\"ipo_access_lower_price\":null,\"is_ipo_access_price_finalized\":false,\"is_visible_to_user\":true,\"has_ipo_access_custom_price_limit\":false,\"is_primary_account\":true}"
          },
          "redirectURL": "https://api.robinhood.com/orders/625df3ee-4a7e-4e17-a128-02177bd4b7da/",


"