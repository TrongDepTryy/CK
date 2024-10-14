import requests

cookies = {
    'store': '162',
    'zone': '2',
    'PHPSESSID': 'inach7atqr5m0tqf09ocb6uisa',
    'cf_clearance': 'uu6LXkiBVbloJGA68.6o_Bssrm3o3LtQRkyCHbWIqB8-1723868128-1.2.1.1-vET5Nb2baafCipDdR_qvrx1y2wUi8izqXIz9VVnAZ7qzwq8T9b9gW7aLbl_CclEg5oZni7sklwq4QCXPQ4kM6TNwUksmuYqWMvfwUPKUTxhJd5K7X.tdwl_fCPC6nDHxXU0pxk3N_L1xzHcse5_e1QQAjWYbTDcQ7MR7PQO6CiAGjk2rZv4jczJIVGjj0rmzvdzIHRFC9ReucK1mDWaaspJc1u8AjsJTO8zDhIE0X0TWJ0sjpFrBFhPG4kGNXCtHBzVtkk3tfukh_o45q0.qeC7ad8Cyy1UH1mLfV9Ney.PcXMKcaGJEueHHQqBIUDxTA6w7ezSB_cOCk3aEScn7gNwugH7EwVQn9cKBZ1Nqy4aOqDc0QfCip9BdSke70VsKg2UXmuO2HL0yrqHpVxDKkA',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8,nb;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'store=162; zone=2; PHPSESSID=inach7atqr5m0tqf09ocb6uisa; cf_clearance=uu6LXkiBVbloJGA68.6o_Bssrm3o3LtQRkyCHbWIqB8-1723868128-1.2.1.1-vET5Nb2baafCipDdR_qvrx1y2wUi8izqXIz9VVnAZ7qzwq8T9b9gW7aLbl_CclEg5oZni7sklwq4QCXPQ4kM6TNwUksmuYqWMvfwUPKUTxhJd5K7X.tdwl_fCPC6nDHxXU0pxk3N_L1xzHcse5_e1QQAjWYbTDcQ7MR7PQO6CiAGjk2rZv4jczJIVGjj0rmzvdzIHRFC9ReucK1mDWaaspJc1u8AjsJTO8zDhIE0X0TWJ0sjpFrBFhPG4kGNXCtHBzVtkk3tfukh_o45q0.qeC7ad8Cyy1UH1mLfV9Ney.PcXMKcaGJEueHHQqBIUDxTA6w7ezSB_cOCk3aEScn7gNwugH7EwVQn9cKBZ1Nqy4aOqDc0QfCip9BdSke70VsKg2UXmuO2HL0yrqHpVxDKkA',
    'origin': 'https://cooponline.vn',
    'priority': 'u=1, i',
    'referer': 'https://cooponline.vn/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'request': 'w_getProductsPosition',
    'store': '162',
    'position': 'homebestsell',
    'term_id': '159',
    'orderby': 'rand',
    'num': '32',
}

response = requests.post('https://cooponline.vn/ajax/', cookies=cookies, headers=headers, data=data)

print(response.json())