from selectolax.lexbor import LexborHTMLParser, LexborNode

html = '<div style="-webkit-text-stroke-width:0px;background-color:rgb(255, 255, 255);color:rgb(32, 33, 36);font-family:docs-Roboto;font-size:14.6667px;font-style:normal;font-variant-caps:normal;font-variant-ligatures:normal;font-weight:400;letter-spacing:normal;orphans:2;text-align:start;text-decoration-color:initial;text-decoration-style:initial;text-decoration-thickness:initial;text-indent:0px;text-transform:none;white-space:normal;widows:2;word-spacing:0px;"><span style="font-family:標楷體;"><span>𖤣 對象：高一高二建中學生</span></span></div><ul style="list-style-type:circle;"><li><div style="-webkit-text-stroke-width:0px;background-color:rgb(255, 255, 255);color:rgb(32, 33, 36);font-family:docs-Roboto;font-size:14.6667px;font-style:normal;font-variant-caps:normal;font-variant-ligatures:normal;font-weight:400;letter-spacing:normal;orphans:2;text-align:start;text-decoration-color:initial;text-decoration-style:initial;text-decoration-thickness:initial;text-indent:0px;text-transform:none;white-space:normal;widows:2;word-spacing:0px;"><span style="background-color:#FFFFCC;color:#C00000;font-family:標楷體;"><u>高一自由報名參加</u></span><span style="background-color:#FFFFCC;color:black;font-family:標楷體;"><span lang="EN-US"><u>(</u></span><strong><u>依報名順序前後優先錄取</u></strong><span lang="EN-US"><u>)</u></span></span></div></li><li><div style="-webkit-text-stroke-width:0px;background-color:rgb(255, 255, 255);color:rgb(32, 33, 36);font-family:docs-Roboto;font-size:14.6667px;font-style:normal;font-variant-caps:normal;font-variant-ligatures:normal;font-weight:400;letter-spacing:normal;orphans:2;text-align:start;text-decoration-color:initial;text-decoration-style:initial;text-decoration-thickness:initial;text-indent:0px;text-transform:none;white-space:normal;widows:2;word-spacing:0px;"><span style="background-color:#FFFFCC;color:black;font-family:標楷體;"><strong>高二優先錄取</strong><span lang="EN-US"><strong>113</strong></span><strong>學年度參與偏鄉英文線上課程計劃的建中學生</strong></span></div></li></ul><div style="-webkit-text-stroke-width:0px;background-color:rgb(255, 255, 255);color:rgb(32, 33, 36);font-family:docs-Roboto;font-size:14.6667px;font-style:normal;font-variant-caps:normal;font-variant-ligatures:normal;font-weight:400;letter-spacing:normal;orphans:2;text-align:start;text-decoration-color:initial;text-decoration-style:initial;text-decoration-thickness:initial;text-indent:0px;text-transform:none;white-space:normal;widows:2;word-spacing:0px;"><span style="font-family:標楷體;"><span>𖤣 人數：約24人</span></span></div><div style="-webkit-text-stroke-width:0px;background-color:rgb(255, 255, 255);color:rgb(32, 33, 36);font-family:docs-Roboto;font-size:14.6667px;font-style:normal;font-variant-caps:normal;font-variant-ligatures:normal;font-weight:400;letter-spacing:normal;orphans:2;text-align:start;text-decoration-color:initial;text-decoration-style:initial;text-decoration-thickness:initial;text-indent:0px;text-transform:none;white-space:normal;widows:2;word-spacing:0px;"><p><span style="font-family:標楷體;"><span>𖤣&nbsp;</span>時間：固定在 <strong>週(四)16:10～17:00 (大小學伴相見歡活動暫訂1210-1700)</strong></span><br><span style="font-family:標楷體;">𖤣&nbsp;地點：建中資源大樓3樓&nbsp;電腦教室(四)</span><br><span style="font-family:標楷體;"><span>𖤣&nbsp;</span>內容：替偏鄉小學生進行線上視訊英文教學</span><br><span style="font-family:標楷體;">𖤣 課程公約：為維持上課品質，請參與同學共同遵守課程約定，若到課情況不佳，將停止該生繼續參與計畫。</span></p><ul style="list-style-type:circle;"><li><span style="font-family:標楷體;"><u>請假最晚須於</u></span><span style="color:red;font-family:標楷體;"><u>上課前一日</u></span><span style="font-family:標楷體;"><u>於群組告知</u>。</span></li><li><span style="font-family:標楷體;"><u>曠課及事假，每學期合計不得超過</u><span lang="EN-US"><u>3</u></span><u>次，嚴重者不核予當學期時數。</u></span></li></ul><p><span style="font-family:標楷體;"><span>𖤣 </span>合作單位：</span><br><span style="font-family:標楷體;">　　一、 新北市瑞芳區九份國民小學</span><br><span style="font-family:標楷體;">　　二、 宜蘭縣五結鄉中興國民小學</span><br><span style="font-family:標楷體;">　　三、 基隆市七堵區復興國民小學</span><br><span style="font-family:標楷體;">　　四、 國際扶輪3481地區偏鄉英文教育委員會</span><br><span style="font-family:標楷體;">𖤣&nbsp;計畫目的：</span><br><span style="font-family:標楷體;">　　一、 透過視訊軟體連線教學，提供偏鄉小學生多元化的認知學習與體驗。</span><br><span style="font-family:標楷體;">　　二、 藉由實體相見歡活動，提供大小學伴實體互動與交流。</span><br><span style="font-family:標楷體;">　　三、 結合服務學習活動，提供小學伴在服務活動中體驗認知學習的重要，並培養大學伴教學相長的機會。</span><br><span style="font-family:標楷體;"><strong>☑</strong>&nbsp; <strong><u>學期結束核實核發公服時數</u></strong>&nbsp;</span></p><div><span style="font-family:標楷體;">&nbsp; 若有同學想了解更多，歡迎洽詢學務處訓育組~楊老師 (<span>☎️分機316)</span></span></div><div><div><span style="font-family:標楷體;"><span>⚡報名人數有限</span><i>(依報名順序錄取 26名，含候補 2名)</i> <strong>113學年度</strong><span><strong>舊生優先保留名額。</strong></span></span></div><div><span style="font-family:標楷體;"><span>⚡報名</span><i>截止日至<strong> 9/1(一)中午13:00 (若人數提前額滿，即關閉表單回覆，若有需求會再公告校網或延長報名時間 )</strong></i><span>。</span></span></div><div><span style="font-family:標楷體;"><span>⚡線上報名請點<strong>→</strong></span></span><a href="https://docs.google.com/forms/d/e/1FAIpQLSd8iO6CMPX7iyhw8JW88bL9s99euTRT5LaJZxjeTLoyaKH-6Q/viewform?usp=dialog" title="" target="_blank" rel="noopener noreferrer"><span style="font-family:標楷體;"><span>114學年度偏鄉英語教育計畫</span></span></a></div><div><span style="font-family:標楷體;">𖤣&nbsp;服務計畫執行時程表</span><span style="color:hsl(240,75%,60%);font-family:標楷體;"><span lang="EN-US"><strong>(</strong></span><strong>如有異動，會於群組告知</strong><span lang="EN-US"><strong>)</strong></span></span><span style="font-family:標楷體;"><strong>：</strong></span></div><p><img src="/uploads/1756177457318GIXE6ngp.jpg" width="600" height="850"></p></div></div>'

parser = LexborHTMLParser(html)

assert parser.body is not None


def parse_elements(ele: LexborNode) -> str:
    texts = []
    for element in ele.iter(include_text=True):
        if element.tag == "-text":
            texts.append(element.text())

        elif element.tag == "a":
            href = element.attributes.get("href", "") or ""  # to satisfy type checker
            texts.append("[" + parse_elements(element) + "](" + href + ")")

        elif element.tag == "b" or element.tag == "strong":
            texts.append("**" + parse_elements(element) + "**")

        elif element.tag == "img":
            src = element.attributes.get("src", "") or ""
            alt = element.attributes.get("alt", "") or ""

            texts.append("![" + alt + "](" + src + ")")

        elif element.tag == "br":
            texts.append("\n")

        elif element.tag == "ul":
            for inner_ele in element.iter(include_text=True):
                texts.append("- " + parse_elements(inner_ele) + "\n")

        elif element.tag == "ol":
            for idx, inner_ele in enumerate(element.iter(include_text=True)):
                texts.append(f"{idx + 1}. " + parse_elements(inner_ele) + "\n")

        else:
            texts.append(parse_elements(element))

    return " ".join(texts).strip()


print(parse_elements(parser.body))
