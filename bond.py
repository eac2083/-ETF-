!pip install -q pykrx tqdm pandas

from pykrx import stock
import pandas as pd, datetime as dt
from tqdm import tqdm

# ① 6자리 티커 24종 (순서는 상관없음)
TICKERS = [
    "426150","439870","438570","152380","397420","302190","114260",
    "363570","356540","385540","278620","336160",
    "484790","305080","468370","456100",
    "182490","332620","332610","458260","468380",
    "459580","449170","455960"
]

# ② 수집 기간
START_DATE = "20080101"
END_DATE   = dt.datetime.today().strftime("%Y%m%d")

# ③ 루프 실행 → CSV 저장
for code in tqdm(TICKERS, desc="ETF 다운로드"):
    try:
        df = stock.get_etf_ohlcv_by_date(START_DATE, END_DATE, code)
        # pykrx 컬럼: 시가·고가·저가·종가·거래량
        df.to_csv(f"{code}_daily_price.csv", encoding="utf-8-sig")
    except Exception as e:
        print(f"[WARN] {code} 실패 ➜ {e}")

print("✅ 모든 ETF 다운로드 완료!")
