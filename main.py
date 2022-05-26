import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager as fm

font_name = fm.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
matplotlib.rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False


# 18년도 평균 평당 가격
def avg_18():
    avg_data = pd.read_csv('./average_data.csv', encoding='cp949', low_memory=False)
    year = 2018
    d_ = avg_data[(avg_data["접수연도"] == year)]
    plt.figure(figsize=(10, 5))
    plt.title("2018년도 평균평당가격", fontsize=15)
    plt.plot(d_["자치구명"], d_["평균평당가격(만원)"], "-", color='red', label=str(year))
    plt.grid()
    plt.legend(fontsize=13)
    plt.xticks(rotation=90)
    plt.show()


# 19년도 평균 평당 가격
def avg_19():
    avg_data = pd.read_csv('./average_data.csv', encoding='cp949', low_memory=False)
    year = 2019
    d_ = avg_data[(avg_data["접수연도"] == year)]
    plt.figure(figsize=(10, 5))
    plt.title("2019년도 평균평당가격", fontsize=15)
    plt.plot(d_["자치구명"], d_["평균평당가격(만원)"], "-", color='red', label=str(year))
    plt.grid()
    plt.legend(fontsize=13)
    plt.xticks(rotation=90)
    plt.show()


# 20년도 평균 평당 가격
def avg_20():
    avg_data = pd.read_csv('./average_data.csv', encoding='cp949', low_memory=False)
    year = 2020
    d_ = avg_data[(avg_data["접수연도"] == year)]
    plt.figure(figsize=(10, 5))
    plt.title("2020년도 평균평당가격", fontsize=15)
    plt.plot(d_["자치구명"], d_["평균평당가격(만원)"], "-", color='red', label=str(year))
    plt.grid()
    plt.legend(fontsize=13)
    plt.xticks(rotation=90)
    plt.show()


# 18년도, 19년도, 20년도 평균 평당 가격 추이
def avg_total():
    avg_data = pd.read_csv('./average_data.csv', encoding='cp949', low_memory=False)
    plt.figure(figsize=(10, 5))
    plt.title("18년도, 19년도, 20년도 평균 평당 가격 추이", fontsize=15)
    for spot_ in [2018, 2019, 2020]:
        d_ = avg_data[(avg_data["접수연도"] == spot_)]
        plt.plot(d_["자치구명"], d_["평균평당가격(만원)"], "-", label=str(spot_), alpha=.6)
    plt.grid()
    plt.legend(fontsize=13)
    plt.xticks(rotation=90)
    plt.show()

# 18년도, 19년도, 20년도 살인 범죄 추이
def kill_total():
    crime_data = pd.read_csv('./crime.csv', encoding='cp949', low_memory=False)
    plt.figure(figsize=(10, 5))
    plt.title("18년도, 19년도, 20년도 살인 범죄 추이", fontsize=15)
    for spot_ in [2018, 2019, 2020]:
        d_ = crime_data[(crime_data["기간"] == spot_)]
        plt.plot(d_["자치구"], d_["살인"], "-", label=str(spot_), alpha=.6)
    plt.grid()
    plt.legend(fontsize=13)
    plt.xticks(rotation=90)
    plt.show()


# 18년도, 19년도, 20년도 강도 범죄 추이
def robbery_total():
    crime_data = pd.read_csv('./crime.csv', encoding='cp949', low_memory=False)
    plt.figure(figsize=(10, 5))
    plt.title("18년도, 19년도, 20년도 강도 범죄 추이", fontsize=15)
    for spot_ in [2018, 2019, 2020]:
        d_ = crime_data[(crime_data["기간"] == spot_)]
        plt.plot(d_["자치구"], d_["강도"], "-", label=str(spot_), alpha=.6)
    plt.grid()
    plt.legend(fontsize=13)
    plt.xticks(rotation=90)
    plt.show()

# 18년도, 19년도, 20년도 강간강제추행 범죄 추이
def molestation_total():
    crime_data = pd.read_csv('./crime.csv', encoding='cp949', low_memory=False)
    plt.figure(figsize=(10, 5))
    plt.title("18년도, 19년도, 20년도 강간강제추행 범죄 추이", fontsize=15)
    for spot_ in [2018, 2019, 2020]:
        d_ = crime_data[(crime_data["기간"] == spot_)]
        plt.plot(d_["자치구"], d_["강간강제추행"], "-", label=str(spot_), alpha=.6)
    plt.grid()
    plt.legend(fontsize=13)
    plt.xticks(rotation=90)
    plt.show()

# 18년도, 19년도, 20년도 절도 범죄 추이
def theft_total():
    crime_data = pd.read_csv('./crime.csv', encoding='cp949', low_memory=False)
    plt.figure(figsize=(10, 5))
    plt.title("18년도, 19년도, 20년도 절도 범죄 추이", fontsize=15)
    for spot_ in [2018, 2019, 2020]:
        d_ = crime_data[(crime_data["기간"] == spot_)]
        plt.plot(d_["자치구"], d_["절도"], "-", label=str(spot_), alpha=.6)
    plt.grid()
    plt.legend(fontsize=13)
    plt.xticks(rotation=90)
    plt.show()


# 18년도, 19년도, 20년도 폭력 범죄 추이
def violence_total():
    crime_data = pd.read_csv('./crime.csv', encoding='cp949', low_memory=False)
    plt.figure(figsize=(10, 5))
    plt.title("18년도, 19년도, 20년도 폭력 범죄 추이", fontsize=15)
    for spot_ in [2018, 2019, 2020]:
        d_ = crime_data[(crime_data["기간"] == spot_)]
        plt.plot(d_["자치구"], d_["폭력"], "-", label=str(spot_), alpha=.6)
    plt.grid()
    plt.legend(fontsize=13)
    plt.xticks(rotation=90)
    plt.show()

# total 강남구 집값과 살인, 강도, 강간강제추행, 절도, 폭력의 상관관계
def crime_Gangnam():
    avg_data = pd.read_csv('./average_data.csv', encoding='cp949', low_memory=False)
    crime_data = pd.read_csv('./crime.csv', encoding='cp949', low_memory=False)
    plt.figure(figsize=(10, 30))

    plt.xticks(rotation=90)
    ax1 = plt.subplot(3, 1, 1)
    ax2 = ax1.twinx()
    d_ = avg_data[(avg_data["자치구명"] == "강남구")]
    a, = ax1.plot(d_["접수연도"], d_["평균평당가격(만원)"], "-", color='red', label="강남구 집값")
    d_ = crime_data[(crime_data["자치구"] == "강남구")]
    b, = ax2.plot(d_["기간"], d_["살인"], "-", color='blue', label="살인율")
    p = [a, b]
    ax1.legend(p, [p_.get_label() for p_ in p])
    plt.title("강남구 집값과 5대 범죄와 상관관계", fontsize=15)

    plt.xticks(rotation=90)
    ax1 = plt.subplot(3, 1, 2)
    ax2 = ax1.twinx()
    d_ = avg_data[(avg_data["자치구명"] == "강남구")]
    a, = ax1.plot(d_["접수연도"], d_["평균평당가격(만원)"], "-", color='red', label="강남구 집값")
    d_ = crime_data[(crime_data["자치구"] == "강남구")]
    b, = ax2.plot(d_["기간"], d_["강도"], "-", color='blue', label="강도")
    p = [a, b]
    ax1.legend(p, [p_.get_label() for p_ in p])

    plt.xticks(rotation=90)
    ax1 = plt.subplot(3, 1, 3)
    ax2 = ax1.twinx()
    d_ = avg_data[(avg_data["자치구명"] == "강남구")]
    a, = ax1.plot(d_["접수연도"], d_["평균평당가격(만원)"], "-", color='red', label="강남구 집값")
    d_ = crime_data[(crime_data["자치구"] == "강남구")]
    b, = ax2.plot(d_["기간"], d_["강간강제추행"], "-", color='blue', label="강간강제추행")
    p = [a, b]
    ax1.legend(p, [p_.get_label() for p_ in p])

    plt.show()

    plt.xticks(rotation=90)
    ax1 = plt.subplot(2, 1, 1)
    ax2 = ax1.twinx()
    d_ = avg_data[(avg_data["자치구명"] == "강남구")]
    a, = ax1.plot(d_["접수연도"], d_["평균평당가격(만원)"], "-", color='red', label="강남구 집값")
    d_ = crime_data[(crime_data["자치구"] == "강남구")]
    b, = ax2.plot(d_["기간"], d_["절도"], "-", color='blue', label="절도")
    p = [a, b]
    ax1.legend(p, [p_.get_label() for p_ in p])

    plt.xticks(rotation=90)
    ax1 = plt.subplot(2, 1, 2)
    ax2 = ax1.twinx()
    d_ = avg_data[(avg_data["자치구명"] == "강남구")]
    a, = ax1.plot(d_["접수연도"], d_["평균평당가격(만원)"], "-", color='red', label="강남구 집값")
    d_ = crime_data[(crime_data["자치구"] == "강남구")]
    b, = ax2.plot(d_["기간"], d_["폭력"], "-", color='blue', label="폭력")
    p = [a, b]
    ax1.legend(p, [p_.get_label() for p_ in p])

    plt.show()

# total 강북구 집값과 살인, 강도, 강간강제추행, 절도, 폭력의 상관관계
def crime_Gangbuk():
    avg_data = pd.read_csv('./average_data.csv', encoding='cp949', low_memory=False)
    crime_data = pd.read_csv('./crime.csv', encoding='cp949', low_memory=False)
    plt.figure(figsize=(10, 30))

    plt.xticks(rotation=90)
    ax1 = plt.subplot(3, 1, 1)
    ax2 = ax1.twinx()
    d_ = avg_data[(avg_data["자치구명"] == "강북구")]
    a, = ax1.plot(d_["접수연도"], d_["평균평당가격(만원)"], "-", color='red', label="강북구 집값")
    d_ = crime_data[(crime_data["자치구"] == "강북구")]
    b, = ax2.plot(d_["기간"], d_["살인"], "-", color='blue', label="살인")
    p = [a, b]
    ax1.legend(p, [p_.get_label() for p_ in p])
    plt.title("강북구 집값과 5대 범죄와 상관관계", fontsize=15)

    plt.xticks(rotation=90)
    ax1 = plt.subplot(3, 1, 2)
    ax2 = ax1.twinx()
    d_ = avg_data[(avg_data["자치구명"] == "강북구")]
    a, = ax1.plot(d_["접수연도"], d_["평균평당가격(만원)"], "-", color='red', label="강북구 집값")
    d_ = crime_data[(crime_data["자치구"] == "강북구")]
    b, = ax2.plot(d_["기간"], d_["강도"], "-", color='blue', label="강도")
    p = [a, b]
    ax1.legend(p, [p_.get_label() for p_ in p])

    plt.xticks(rotation=90)
    ax1 = plt.subplot(3, 1, 3)
    ax2 = ax1.twinx()
    d_ = avg_data[(avg_data["자치구명"] == "강북구")]
    a, = ax1.plot(d_["접수연도"], d_["평균평당가격(만원)"], "-", color='red', label="강북구 집값")
    d_ = crime_data[(crime_data["자치구"] == "강북구")]
    b, = ax2.plot(d_["기간"], d_["강간강제추행"], "-", color='blue', label="강간강제추행")
    p = [a, b]
    ax1.legend(p, [p_.get_label() for p_ in p])

    plt.show()

    plt.xticks(rotation=90)
    ax1 = plt.subplot(2, 1, 1)
    ax2 = ax1.twinx()
    d_ = avg_data[(avg_data["자치구명"] == "강북구")]
    a, = ax1.plot(d_["접수연도"], d_["평균평당가격(만원)"], "-", color='red', label="강북구 집값")
    d_ = crime_data[(crime_data["자치구"] == "강북구")]
    b, = ax2.plot(d_["기간"], d_["절도"], "-", color='blue', label="절도")
    p = [a, b]
    ax1.legend(p, [p_.get_label() for p_ in p])

    plt.xticks(rotation=90)
    ax1 = plt.subplot(2, 1, 2)
    ax2 = ax1.twinx()
    d_ = avg_data[(avg_data["자치구명"] == "강북구")]
    a, = ax1.plot(d_["접수연도"], d_["평균평당가격(만원)"], "-", color='red', label="강북구 집값")
    d_ = crime_data[(crime_data["자치구"] == "강북구")]
    b, = ax2.plot(d_["기간"], d_["폭력"], "-", color='blue', label="폭력")
    p = [a, b]
    ax1.legend(p, [p_.get_label() for p_ in p])

    plt.show()

# total 구로구 집값과 살인, 강도, 강간강제추행, 절도, 폭력의 상관관계
def crime_Guro():
    avg_data = pd.read_csv('./average_data.csv', encoding='cp949', low_memory=False)
    crime_data = pd.read_csv('./crime.csv', encoding='cp949', low_memory=False)
    plt.figure(figsize=(10, 30))

    plt.xticks(rotation=90)
    ax1 = plt.subplot(3, 1, 1)
    ax2 = ax1.twinx()
    d_ = avg_data[(avg_data["자치구명"] == "구로구")]
    a, = ax1.plot(d_["접수연도"], d_["평균평당가격(만원)"], "-", color='red', label="구로구 집값")
    d_ = crime_data[(crime_data["자치구"] == "구로구")]
    b, = ax2.plot(d_["기간"], d_["살인"], "-", color='blue', label="살인")
    p = [a, b]
    ax1.legend(p, [p_.get_label() for p_ in p])
    plt.title("구로구 집값과 5대 범죄와 상관관계", fontsize=15)

    plt.xticks(rotation=90)
    ax1 = plt.subplot(3, 1, 2)
    ax2 = ax1.twinx()
    d_ = avg_data[(avg_data["자치구명"] == "구로구")]
    a, = ax1.plot(d_["접수연도"], d_["평균평당가격(만원)"], "-", color='red', label="구로구 집값")
    d_ = crime_data[(crime_data["자치구"] == "구로구")]
    b, = ax2.plot(d_["기간"], d_["강도"], "-", color='blue', label="강도")
    p = [a, b]
    ax1.legend(p, [p_.get_label() for p_ in p])

    plt.xticks(rotation=90)
    ax1 = plt.subplot(3, 1, 3)
    ax2 = ax1.twinx()
    d_ = avg_data[(avg_data["자치구명"] == "구로구")]
    a, = ax1.plot(d_["접수연도"], d_["평균평당가격(만원)"], "-", color='red', label="구로구 집값")
    d_ = crime_data[(crime_data["자치구"] == "구로구")]
    b, = ax2.plot(d_["기간"], d_["강간강제추행"], "-", color='blue', label="강간강제추행")
    p = [a, b]
    ax1.legend(p, [p_.get_label() for p_ in p])

    plt.show()

    plt.xticks(rotation=90)
    ax1 = plt.subplot(2, 1, 1)
    ax2 = ax1.twinx()
    d_ = avg_data[(avg_data["자치구명"] == "구로구")]
    a, = ax1.plot(d_["접수연도"], d_["평균평당가격(만원)"], "-", color='red', label="구로구 집값")
    d_ = crime_data[(crime_data["자치구"] == "구로구")]
    b, = ax2.plot(d_["기간"], d_["절도"], "-", color='blue', label="절도")
    p = [a, b]
    ax1.legend(p, [p_.get_label() for p_ in p])

    plt.xticks(rotation=90)
    ax1 = plt.subplot(2, 1, 2)
    ax2 = ax1.twinx()
    d_ = avg_data[(avg_data["자치구명"] == "구로구")]
    a, = ax1.plot(d_["접수연도"], d_["평균평당가격(만원)"], "-", color='red', label="구로구 집값")
    d_ = crime_data[(crime_data["자치구"] == "구로구")]
    b, = ax2.plot(d_["기간"], d_["폭력"], "-", color='blue', label="폭력")
    p = [a, b]
    ax1.legend(p, [p_.get_label() for p_ in p])

    plt.show()

# total 마포구 집값과 살인, 강도, 강간강제추행, 절도, 폭력의 상관관계
def crime_Mapo():
    avg_data = pd.read_csv('./average_data.csv', encoding='cp949', low_memory=False)
    crime_data = pd.read_csv('./crime.csv', encoding='cp949', low_memory=False)
    plt.figure(figsize=(10, 30))

    plt.xticks(rotation=90)
    ax1 = plt.subplot(3, 1, 1)
    ax2 = ax1.twinx()
    d_ = avg_data[(avg_data["자치구명"] == "마포구")]
    a, = ax1.plot(d_["접수연도"], d_["평균평당가격(만원)"], "-", color='red', label="마포구 집값")
    d_ = crime_data[(crime_data["자치구"] == "마포구")]
    b, = ax2.plot(d_["기간"], d_["살인"], "-", color='blue', label="살인")
    p = [a, b]
    ax1.legend(p, [p_.get_label() for p_ in p])
    plt.title("마포구 집값과 5대 범죄와 상관관계", fontsize=15)

    plt.xticks(rotation=90)
    ax1 = plt.subplot(3, 1, 2)
    ax2 = ax1.twinx()
    d_ = avg_data[(avg_data["자치구명"] == "마포구")]
    a, = ax1.plot(d_["접수연도"], d_["평균평당가격(만원)"], "-", color='red', label="마포구 집값")
    d_ = crime_data[(crime_data["자치구"] == "마포구")]
    b, = ax2.plot(d_["기간"], d_["강도"], "-", color='blue', label="강도")
    p = [a, b]
    ax1.legend(p, [p_.get_label() for p_ in p])

    plt.xticks(rotation=90)
    ax1 = plt.subplot(3, 1, 3)
    ax2 = ax1.twinx()
    d_ = avg_data[(avg_data["자치구명"] == "마포구")]
    a, = ax1.plot(d_["접수연도"], d_["평균평당가격(만원)"], "-", color='red', label="마포구 집값")
    d_ = crime_data[(crime_data["자치구"] == "마포구")]
    b, = ax2.plot(d_["기간"], d_["강간강제추행"], "-", color='blue', label="강간강제추행")
    p = [a, b]
    ax1.legend(p, [p_.get_label() for p_ in p])

    plt.show()

    plt.xticks(rotation=90)
    ax1 = plt.subplot(2, 1, 1)
    ax2 = ax1.twinx()
    d_ = avg_data[(avg_data["자치구명"] == "마포구")]
    a, = ax1.plot(d_["접수연도"], d_["평균평당가격(만원)"], "-", color='red', label="마포구 집값")
    d_ = crime_data[(crime_data["자치구"] == "마포구")]
    b, = ax2.plot(d_["기간"], d_["절도"], "-", color='blue', label="절도")
    p = [a, b]
    ax1.legend(p, [p_.get_label() for p_ in p])

    plt.xticks(rotation=90)
    ax1 = plt.subplot(2, 1, 2)
    ax2 = ax1.twinx()
    d_ = avg_data[(avg_data["자치구명"] == "마포구")]
    a, = ax1.plot(d_["접수연도"], d_["평균평당가격(만원)"], "-", color='red', label="마포구 집값")
    d_ = crime_data[(crime_data["자치구"] == "마포구")]
    b, = ax2.plot(d_["기간"], d_["폭력"], "-", color='blue', label="폭력")
    p = [a, b]
    ax1.legend(p, [p_.get_label() for p_ in p])

    plt.show()

# total 종로구 집값과 살인, 강도, 강간강제추행, 절도, 폭력의 상관관계
def crime_Jongro():
    avg_data = pd.read_csv('./average_data.csv', encoding='cp949', low_memory=False)
    crime_data = pd.read_csv('./crime.csv', encoding='cp949', low_memory=False)
    plt.figure(figsize=(10, 30))

    plt.xticks(rotation=90)
    ax1 = plt.subplot(3, 1, 1)
    ax2 = ax1.twinx()
    d_ = avg_data[(avg_data["자치구명"] == "종로구")]
    a, = ax1.plot(d_["접수연도"], d_["평균평당가격(만원)"], "-", color='red', label="종로구 집값")
    d_ = crime_data[(crime_data["자치구"] == "종로구")]
    b, = ax2.plot(d_["기간"], d_["살인"], "-", color='blue', label="살인")
    p = [a, b]
    ax1.legend(p, [p_.get_label() for p_ in p])
    plt.title("종로구 집값과 5대 범죄와 상관관계", fontsize=15)

    plt.xticks(rotation=90)
    ax1 = plt.subplot(3, 1, 2)
    ax2 = ax1.twinx()
    d_ = avg_data[(avg_data["자치구명"] == "종로구")]
    a, = ax1.plot(d_["접수연도"], d_["평균평당가격(만원)"], "-", color='red', label="종로구 집값")
    d_ = crime_data[(crime_data["자치구"] == "종로구")]
    b, = ax2.plot(d_["기간"], d_["강도"], "-", color='blue', label="강도")
    p = [a, b]
    ax1.legend(p, [p_.get_label() for p_ in p])

    plt.xticks(rotation=90)
    ax1 = plt.subplot(3, 1, 3)
    ax2 = ax1.twinx()
    d_ = avg_data[(avg_data["자치구명"] == "종로구")]
    a, = ax1.plot(d_["접수연도"], d_["평균평당가격(만원)"], "-", color='red', label="종로구 집값")
    d_ = crime_data[(crime_data["자치구"] == "종로구")]
    b, = ax2.plot(d_["기간"], d_["강간강제추행"], "-", color='blue', label="강간강제추행")
    p = [a, b]
    ax1.legend(p, [p_.get_label() for p_ in p])

    plt.show()

    plt.xticks(rotation=90)
    ax1 = plt.subplot(2, 1, 1)
    ax2 = ax1.twinx()
    d_ = avg_data[(avg_data["자치구명"] == "종로구")]
    a, = ax1.plot(d_["접수연도"], d_["평균평당가격(만원)"], "-", color='red', label="종로구 집값")
    d_ = crime_data[(crime_data["자치구"] == "종로구")]
    b, = ax2.plot(d_["기간"], d_["절도"], "-", color='blue', label="절도")
    p = [a, b]
    ax1.legend(p, [p_.get_label() for p_ in p])

    plt.xticks(rotation=90)
    ax1 = plt.subplot(2, 1, 2)
    ax2 = ax1.twinx()
    d_ = avg_data[(avg_data["자치구명"] == "종로구")]
    a, = ax1.plot(d_["접수연도"], d_["평균평당가격(만원)"], "-", color='red', label="종로구 집값")
    d_ = crime_data[(crime_data["자치구"] == "종로구")]
    b, = ax2.plot(d_["기간"], d_["폭력"], "-", color='blue', label="폭력")
    p = [a, b]
    ax1.legend(p, [p_.get_label() for p_ in p])

    plt.show()

def main():
    # avg_18()
    # avg_19()
    # avg_20()
    # avg_total()
    # kill_total()
    # robbery_total()
    # molestation_total()
    # theft_total()
    # violence_total()
    # crime_Gangnam()
    # crime_Gangbuk()
    # crime_Guro()
    # crime_Mapo()
     crime_Jongro()

if __name__ == '__main__':
    main()
