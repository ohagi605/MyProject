word = [
    # あ行
    "あめ", "いぬ", "うし", "えのぐ", "おかし",
    # か行
    "かさ", "きつね", "くるま", "けむし", "こおり",
    # が行
    "がまぐち", "ぎんが", "ぐんま", "げんき", "ごま",
    # さ行
    "さくら", "しお", "すいか", "せみ", "そら",
    # ざ行
    "ざりがに", "じしょ", "ずこう", "ぜんまい", "ぞう",
    # た行
    "たまご", "ちず", "つばさ", "てがみ", "とけい",
    # だ行
    "だるま", "ぢから", "づつう", "でんき", "どろ",
    # な行
    "なみ", "にじ", "ぬの", "ねこ", "のはら",
    # は行
    "はな", "ひと", "ふね", "へや", "ほし",
    # ば行
    "ばら", "びーる", "ぶた", "べんきょう", "ぼうし",
    # ぱ行
    "ぱん", "ぴあの", "ぷーる", "ぺんぎん", "ぽけっと",
    # ま行
    "まど", "みず", "むし", "めがね", "もり",
    # や行
    "やま", "ゆき", "よる",
    # ら行
    "らくだ", "りす", "るす", "れんげ", "ろうそく",
    # わ行
    "わに", "をの", "ん"
]

c = 0
print("しりとりスタート！！")

while True:    
    n = input()
    if n != "end":
        if n[-1] == 'ん': break
        else:
            for i in word:
                if n[-1] == i[0]:
                    print(i);c += 1
                    if c % 3 == 0:
                        print("（いい調子です(o^―^o)ﾆｺ）");break
    else:
        print("遊んでくれてありがとう！！"+str(c*2)+"個続きました！")
        break
