import requests
import json

# 1. API URL (path + scheme + authority)
# cursor 값과 page-size는 크롤링 페이지에 따라 변경되어야 합니다.
api_url = "https://search.shopping.naver.com/ns/v1/search/paged-composite-cards?cursor=35&pageSize=50&query=%EB%82%98%EC%9D%B4%ED%82%A4%20%EC%9A%B4%EB%8F%99%ED%99%94&searchMethod=all.basic&isFreshCategory=false&isOriginalQuerySearch=false&isCatalogDiversifyOff=true&listPage=2&previousSMESlotNvMids=85590865857&categoryIdsForPromotions=50000173&categoryIdsForPromotions=50000174&categoryIdsForPromotions=50000139&categoryIdsForPromotions=50000175&categoryIdsForPromotions=50000052&hiddenNonProductCard=false&duplicatedNvMids=85590865857&hasMoreAd=true&hasMore=true"

# 2. 모든 요청 헤더 (쿠키 포함)
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Content-Type": "application/json",
    # !!! 쿠키 값은 매우 중요하지만, 유효 기간이 있으므로 크롤링 시점마다 업데이트가 필요합니다. !!!
    "Cookie": "NNB=2PSTGP66PKKGM; SHP_BUCKET_ID=0; ASID=3b13e7c30000019405ef3db90000004c; nstore_session=XjdmKzvSNdS5pma/XgLhRXyS; _fbp=fb.1.1760330955624.647167482479724957; _ga=GA1.1.155369223.1760330956; _ga_EFBDNNF91G=GS2.1.s1760330956$o1$g0$t1760330959$j57$l0$h0; ncpa=10295434|mgq54dao|a08e90e29e494542db2404ee01b7322befbc0fbd|s_e4574dbfb237|250aba18af0e1e931bc92bbac2883a77e3758433; NACT=1; SRT30=1760600060; NAC=mCWPB0QKmeI3A; SRT5=1760602148; nstore_pagesession=jnuo7lqrczXBLssMfpd-311691; RELATED_PRODUCT=ON; OEP_CONFIG=[{%22serId%22:%22shopping%22%2C%22type%22:%22oep%22%2C%22expId%22:%22NEWS-CROP-IMG%22%2C%22varId%22:%222%22%2C%22value%22:{%22bt%22:%222%22%2C%22is_control%22:true}%2C%22userType%22:%22nnb%22%2C%22provId%22:%22%22%2C%22sesnId%22:%22%22}%2C{%22serId%22:%22shopping%22%2C%22type%22:%22oep%22%2C%22expId%22:%22PWL-SAS-RPRV%22%2C%22varId%22:%223%22%2C%22value%22:{%22bucket%22:%222%22%2C%22is_control%22:false}%2C%22userType%22:%22nnb%22%2C%22provId%22:%22%22%2C%22sesnId%22:%22%22}]; BUC=NmVVK3Rv3lRg5oeuxrAP7-JhrRGDb1dQRpvYaCt11wE=",
    "Priority": "u=1, i",
    "Referer": "https://search.shopping.naver.com/ns/search?query=%EB%82%98%EC%9D%B4%ED%82%A4%20%EC%9A%B4%EB%8F%99%ED%99%94",
    "Sec-Ch-Ua": '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    "Sec-Ch-Ua-Arch": '"x86"',
    "Sec-Ch-Ua-Bitness": '"64"',
    "Sec-Ch-Ua-Form-Factors": '"Desktop"',
    "Sec-Ch-Ua-Full-Version-List": '"Google Chrome";v="141.0.7390.76", "Not?A_Brand";v="8.0.0.0", "Chromium";v="141.0.7390.76"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Model": '""',
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Ch-Ua-Platform-Version": '"19.0.0"',
    "Sec-Ch-Ua-Wow64": "?0",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}

try:
    # 요청 전송
    response = requests.get(api_url, headers=headers, timeout=15)

    if response.status_code == 200:
        print("✅ API 요청 성공. JSON 데이터를 수신했습니다.")
        # 데이터가 JSON 형식인지 확인 후 파싱
        data = response.json()

        # response는 API 요청 성공 시 받은 requests.Response 객체입니다.
        data = response.json()

        # indent=4를 사용하여 4칸 들여쓰기로 출력
        print(json.dumps(data, indent=4, ensure_ascii=False))
    elif response.status_code == 403:
        print("❌ 요청이 403 Forbidden으로 여전히 차단되었습니다.")
        print("이는 쿠키 또는 세션 토큰이 만료되었거나, 서버가 IP를 차단했음을 의미합니다.")
    else:
        print(f"⚠️ API 요청 실패. 상태 코드: {response.status_code}")
        print("응답 내용:", response.text[:500]) # 응답 내용을 일부 출력하여 실패 원인 확인
        
except requests.exceptions.RequestException as e:
    print(f"🚨 요청 중 오류 발생: {e}")

# 연속 요청 방지
import time
time.sleep(2)