import requests

headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

data = 'billing_details[name]=Hdhaj+chajd+&billing_details[address][country]=IQ&billing_details[address][state]=CA&billing_details[email]=oentokes%40gmail.com&billing_details[phone]=9647803185991&type=card&card[number]=5425+3950+3283+5092&card[cvc]=166&card[exp_year]=28&card[exp_month]=10&allow_redisplay=unspecified&pasted_fields=number&payment_user_agent=stripe.js%2F4094b7b36a%3B+stripe-js-v3%2F4094b7b36a%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fdietncheat.com&time_on_page=142491&client_attribution_metadata[client_session_id]=5d874689-85f6-46c9-8397-3aa5eeb117f2&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&guid=341e2f6b-0cb9-4836-bbe1-ca68e88dd0983fa1fb&muid=382c5f59-fc22-44b1-a5ed-dc6375963fc05a8183&sid=3dc04748-1468-48ce-b5ae-2b7e72fa6fa73a3487&key=pk_live_51MUTt7ApSs8qX1u0i0TBr2Lf8B70QXQcrVl1wEILPDzZvecVGqKTH8CXSvxG6EvR9w0IsXi9GBbY3Mnr79tNGrDo00aqSaONHk&_stripe_account=acct_1MUTt7ApSs8qX1u0&_stripe_version=2022-08-01&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQZGaUqaxToGk9aYtPQBlWuU4TT7zYo6fkFhAiPoeGwJdY4s5Icnh1s4nkegMqY1bAv8H6Zr_reyN_9p_MIJK3x4VT3iEzhy2d20cv8QoTxPuTS5CIsCqyr0XgDg9v_jjPdXSNKHsMiOH6dLxzIegJAorB_cX48jjlAdmVYJqXmiKclwcKVJxrgeJM9A3ZG0Bqmuxtj6oiNu0FDN80lLMTGWD9nlFkyJ5fzeV_xwJ6UMzotJ7zFoRDRmC0QakakAyWMXM-dqRVMVZCrjYDniHe6bu4F_IWuOKvTiIWaw4jdnoj4wU_4hJGBuSlg48ojLnfPvEokuKWEZ_OC6-4MFSsBauOWUMXqNhurRx5Z8YE2iEgxOgtzRv3y-KxGyX2NHGs80jt0FyDu59Vx17tn6lgYIjWKl613m9sYnvAcTNJICbedrhtZwN9Onk-n-Cbr6lwdGoo0P-9HRa5KPQKT33XHMHITXpUQDvOtOPb-q26K6R6PhPw5LmDnby8vkAJRvE6CBWIMaC5Y2JLAMAY9-lQJTZf2yaJ8pjYEjE1WrKRnKoCF84FSj3Y2k_u6NsJFxWmTOUI4sPi-asuANu6jG8qxqE-61RAzIRxiTlkMGDgtdO7eES_Q8rGwtLOEwfFWHwDoZWdXQsE-q_YlW2LGnZ9Xsh6dYEN0H4ioTg4QWswP4RUF6BR39lIR7Z_W0qBTnu28P99-OxJHaxGAp4EYVsm7vn3dOnZPxBWg0LGpbMU6484FBGlV3btUld8JbvToM1DJ3KSbwtwe1disJjbsCbKm8ZGkP4ZJUMJs9hfRP219HGWbYueZUSOhzP1mPLBjQv1alKTQZPLHzQkwLSsYQPFr2G9nfsRbt665eVzLBNh-xc96jiJEzmEFr_ma56F9A3TPd3lV2C2ZgeLRdAl42rr3kgQ6AndNSJLnsPd0Y67exo22s1sdAi0f2rF2SApU_LLj0iMiCtRV92-07ZVS6hmG-OM27FFnJY1e4W-Ba-DbQ-Cod5udlMPpNbMEjoHa6fOvP53J4-UdRk2YD5gWl8NWqCiWwIgG5OS-lhShIPpmkdJ9N7cqagxpDmbaXU9OJy7VWh9rpazWFItjE78S0quYN6u5a6459coxRxh01iu55amRMltbVWJ02KO0Y5tYr5kHu210MT1Lk8XG8QvAQwoFGU4YCQ7_crAs52r8niQLNItFDwlcH-PlvjO82HiFTg4iXwNQPA9XVesDRylc-b7S9SijnKJVmST5ZlRDPlkSGdOheHXJpglDP7BrbbEthMb_Ub1Ko-qHtoWi2ZvsqGZ_gXh_VtrglmXv_IPvO1mWi0B14fDVD6Fwfk37O4PvE3E9fvWHRjevEHOcV9xndbJtTRx_Kz55qcg31T-LzLbVeOWF08MPDZqNM0Ayrj-xuz1hLITtIeb06avynj9TK5oETZuggX1fBHbqDc4D-fso5OZ3BCvDcT0t3ggD8ZmeybJbxd9sCLO8AlIZeTiNZHkFysVF1Z54vybxjPLOqW2aFREHWNkLsheHJGsp9r7en40k18Hdd7I1Nl25E1XCCV1Dox0IAeUjZTOWTKb14-kpEfxW_cg5na6LJ3WqZ4-1dlQTei0dgTBqCfQ6gbHii8ocuQTWOtcsnHyPjWyHRsnNJ7joAPuZwYtH_1IZxxO2R94kBTGlvyFiXyKhS1GouGs-jqYQBWacTrEpZNHJzAQsOsY4yK5Y0KpsUf10xMRvDifZxBRQACfZ_muCB1vDsRW5RkWeV-Mrt8-Vv4Qbr1pnOCPNEK9PHbTehSRttsQsDYDqkuyK8H5lDhPfG2HGSwT2Xutv_3bTgI2PmbPhg__35t__FImH1N70jFHQbQbUpnPP5eGf6MiaGd5pVphLczQE-qbYfw7l8AWubFHGt15sMvQY_ZESQiXQBSkhFTw3cRBgrJUdJep2Q5MUa5Fg-FvVBGwZ2gHhpDoWHCvyoGAUBf5E8g0trDAcfM3XNDcjQVYUJ2-NJx1lJrc_Dzo4WX015KbUabm0WGxwoZwNR1A8KZ37I4NUBqKY7VgUB99G0X2EPo_75FN2OEugRCASIjba3hJgXsqu71izEFHOqX3u2leYuPJlXEG7FEl1F1ELeKcgGLgF10kECRwwVVskT3ebSiIqftO0Vu6NleHDOZi9TUqhzaGFyZF9pZM4DMYNvomtyqDIzZjc2YzJionBkAA.PSs1uzKbBYgQ9hRyer0Z9dwlSADrEJ-WYXyBXnpawes'

response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
id=response.json()['id']
import requests

cookies = {
    'woocommerce_items_in_cart': '1',
    'pll_language': 'en',
    'woocommerce_cart_hash': '19a7dfa93d708845d4eed8af6d1daac4',
    'PHPSESSID': 'vvcoiu7v266v83vbu5cu06i7ui',
    'wp_woocommerce_session_e03f3775a42657fc58cf7fb79c6a8510': 't_147ffdbefbb3528ae1c1f605e339e3%7C%7C1714550085%7C%7C1714546485%7C%7C1ad2ddb34b70a4d197c4e6843d841426',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-04-29%2007%3A54%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fdietncheat.com%2Fcheckouts%2Fbudget-1%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-04-29%2007%3A54%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fdietncheat.com%2Fcheckouts%2Fbudget-1%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fdietncheat.com%2Fcheckouts%2Fbudget-1%2F',
    '_gcl_au': '1.1.2016540396.1714377290',
    'wffn_flt': '2024-4-29 07:54:50',
    'wffn_timezone': 'Asia/Baghdad',
    'wffn_is_mobile': 'true',
    'wffn_browser': 'Chrome',
    'wffn_referrer': '',
    'wffn_fl_url': '/checkouts/budget-1/',
    '_ga': 'GA1.1.1647868886.1714377292',
    '_fbp': 'fb.1.1714377293109.1189033502',
    'wffn_si': '964750700753356ca508d254a91a31cf',
    'uael-timer-cdTime-3504edf': '1714463697525',
    'uael-timer-evgInt-3504edf': '86400000',
    'uael-timer-firstTime-3504edf': '1714377297525',
    'uael-time-to-run-3504edf': '1714463697512',
    'uael-timer-cdTime-33eea6b': '1714463697596',
    'uael-timer-evgInt-33eea6b': '86400000',
    'uael-timer-firstTime-33eea6b': '1714377297596',
    'uael-time-to-run-33eea6b': '1714463697585',
    'uael-timer-days-3504edf': '0',
    'uael-timer-hours-3504edf': '23',
    'uael-timer-days-33eea6b': '0',
    'uael-timer-hours-33eea6b': '23',
    '_scid': '2716e186-38d1-4f4d-9f9c-1505edcf4399',
    '_scid_r': '2716e186-38d1-4f4d-9f9c-1505edcf4399',
    '_tt_enable_cookie': '1',
    '_ttp': 'At5A2Pck3r858iZfeb27O4RqIo0',
    '__stripe_mid': '382c5f59-fc22-44b1-a5ed-dc6375963fc05a8183',
    '__stripe_sid': '3dc04748-1468-48ce-b5ae-2b7e72fa6fa73a3487',
    'wfocu_si': '0c2f39990fc4030b573426d009cb06f2',
    '_ga_LG0G3025ZY': 'GS1.1.1714377292.1.1.1714377306.46.0.1970502599',
    'bwfan_session': '1',
    'bwfan_visitor': 'WJuY84saghlaKual',
    'wffn_ay_964750700753356ca508d254a91a31cf': '[11766]',
    '_sctr': '1%7C1714338000000',
    '_fk_contact_uid': '25100a0942ba4ccca36317d1de3af712',
    'uael-timer-minutes-3504edf': '57',
    'uael-timer-minutes-33eea6b': '57',
    'uael-timer-distance-3504edf': '86263699',
    'uael-timer-seconds-3504edf': '43',
    'uael-timer-distance-33eea6b': '86263717',
    'uael-timer-seconds-33eea6b': '43',
}

headers = {
    'authority': 'dietncheat.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'woocommerce_items_in_cart=1; pll_language=en; woocommerce_cart_hash=19a7dfa93d708845d4eed8af6d1daac4; PHPSESSID=vvcoiu7v266v83vbu5cu06i7ui; wp_woocommerce_session_e03f3775a42657fc58cf7fb79c6a8510=t_147ffdbefbb3528ae1c1f605e339e3%7C%7C1714550085%7C%7C1714546485%7C%7C1ad2ddb34b70a4d197c4e6843d841426; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-04-29%2007%3A54%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fdietncheat.com%2Fcheckouts%2Fbudget-1%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-04-29%2007%3A54%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fdietncheat.com%2Fcheckouts%2Fbudget-1%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fdietncheat.com%2Fcheckouts%2Fbudget-1%2F; _gcl_au=1.1.2016540396.1714377290; wffn_flt=2024-4-29 07:54:50; wffn_timezone=Asia/Baghdad; wffn_is_mobile=true; wffn_browser=Chrome; wffn_referrer=; wffn_fl_url=/checkouts/budget-1/; _ga=GA1.1.1647868886.1714377292; _fbp=fb.1.1714377293109.1189033502; wffn_si=964750700753356ca508d254a91a31cf; uael-timer-cdTime-3504edf=1714463697525; uael-timer-evgInt-3504edf=86400000; uael-timer-firstTime-3504edf=1714377297525; uael-time-to-run-3504edf=1714463697512; uael-timer-cdTime-33eea6b=1714463697596; uael-timer-evgInt-33eea6b=86400000; uael-timer-firstTime-33eea6b=1714377297596; uael-time-to-run-33eea6b=1714463697585; uael-timer-days-3504edf=0; uael-timer-hours-3504edf=23; uael-timer-days-33eea6b=0; uael-timer-hours-33eea6b=23; _scid=2716e186-38d1-4f4d-9f9c-1505edcf4399; _scid_r=2716e186-38d1-4f4d-9f9c-1505edcf4399; _tt_enable_cookie=1; _ttp=At5A2Pck3r858iZfeb27O4RqIo0; __stripe_mid=382c5f59-fc22-44b1-a5ed-dc6375963fc05a8183; __stripe_sid=3dc04748-1468-48ce-b5ae-2b7e72fa6fa73a3487; wfocu_si=0c2f39990fc4030b573426d009cb06f2; _ga_LG0G3025ZY=GS1.1.1714377292.1.1.1714377306.46.0.1970502599; bwfan_session=1; bwfan_visitor=WJuY84saghlaKual; wffn_ay_964750700753356ca508d254a91a31cf=[11766]; _sctr=1%7C1714338000000; _fk_contact_uid=25100a0942ba4ccca36317d1de3af712; uael-timer-minutes-3504edf=57; uael-timer-minutes-33eea6b=57; uael-timer-distance-3504edf=86263699; uael-timer-seconds-3504edf=43; uael-timer-distance-33eea6b=86263717; uael-timer-seconds-33eea6b=43',
    'origin': 'https://dietncheat.com',
    'referer': 'https://dietncheat.com/checkouts/budget-1/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'wc-ajax': 'checkout',
    'wfacp_id': '11766',
    'wfacp_is_checkout_override': 'no',
}

data = '_wfacp_post_id=11766&wfacp_cart_hash=a2dab33bb5303f54f4229a0f8386ec5c&wfacp_has_active_multi_checkout=&wfacp_source=https%3A%2F%2Fdietncheat.com%2Fcheckouts%2Fbudget-1%2F&product_switcher_need_refresh=1&wfacp_cart_contains_subscription=0&wfacp_exchange_keys=%7B%22pre_built%22%3A%7B%7D%2C%22elementor%22%3A%7B%22wfacp_form%22%3A%221acc80b%22%2C%22wfacp_form_summary%22%3A%221710c48e%22%7D%7D&wfacp_input_hidden_data=%7B%7D&wfacp_input_phone_field=%7B%7D&wfacp_timezone=Asia%2FBaghdad&billing_country=IQ&wfob_input_hidden_data=%7B%7D&billing_email=oentokes%40gmail.com&bwfan_cart_id=18596&billing_first_name=Hdhaj+chajd&billing_phone=9647803185991&wfacp_product_choosen=on&wfacp_product_switcher_quantity_wfacp_64c34cb73b38a=1&payment_method=stripe_cc&stripe_cc_token_key=pm_1PAp5KApSs8qX1u0XJ4tj895&stripe_cc_payment_intent_key=&terms=1&terms-field=1&bwfan_user_consent=1&woocommerce-process-checkout-nonce=320d21104d&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review%26wfacp_id%3D11766%26wfacp_is_checkout_override%3Dno&wc_order_attribution_source_type=typein&wc_order_attribution_referrer=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fdietncheat.com%2Fcheckouts%2Fbudget-1%2F&wc_order_attribution_session_start_time=2024-04-29+07%3A54%3A49&wc_order_attribution_session_pages=1&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+(Linux%3B+Android+10%3B+K)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F124.0.0.0+Mobile+Safari%2F537.36&wc_order_attribution_source_type=typein&wc_order_attribution_referrer=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fdietncheat.com%2Fcheckouts%2Fbudget-1%2F&wc_order_attribution_session_start_time=2024-04-29+07%3A54%3A49&wc_order_attribution_session_pages=1&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+(Linux%3B+Android+10%3B+K)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F124.0.0.0+Mobile+Safari%2F537.36'

response = requests.post('https://dietncheat.com/', params=params, cookies=cookies, headers=headers, data=data)
print(response.json())