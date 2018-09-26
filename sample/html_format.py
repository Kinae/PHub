html = '<html><head><style>div.gallery{margin: 5px;border: 1px solid #ccc; float: left; width: ' \
       '180px;}div.gallery:hover{border: 1px solid #777;}div.gallery img{width: 100%; height: auto;}div.desc{padding: ' \
       '15px; text-align: center;}div.container{position: relative;}div.text-block-bottom-left{font-size: 10px; ' \
       'position: absolute; bottom: 0px; right: 0px; background-color: transparent; color: white; padding-left: 2px; ' \
       'padding-right: 2px;}</style></head><body>$body</body></html>'

body = '<div class="gallery"> <a target="_blank" href="$href"> <div class="container"> <img src="$img" width="300" ' \
       'height="200"><div class="text-block-bottom-right"> <p>$duration</p></div></div><div ' \
       'class="text-block-top-right"> <p>$quality</p></div></div><div class="text-block-bottom-left"> ' \
       '<p>$vote</p></div></div></a> <div class="desc">$title</div><div class="desc">$views $verified ' \
       '$time</div></div> '


def create(result_by_keyword):
    body_str = ''
    for keyword in result_by_keyword:
        body_filled = body.replace('$href', 'https://fr.pornhub.com/view_video.php?viewkey=' + result_by_keyword[keyword]['VIDEO_KEY'])
        body_filled = body_filled.replace('$img', result_by_keyword[keyword]['IMAGE'])
        body_filled = body_filled.replace('$duration', result_by_keyword[keyword]['DURATION'])
        body_filled = body_filled.replace('$quality', result_by_keyword[keyword]['QUALITY'])
        body_filled = body_filled.replace('$title', result_by_keyword[keyword]['TITLE'])
        body_filled = body_filled.replace('$vote', result_by_keyword[keyword]['VOTE'])
        body_filled = body_filled.replace('$views', result_by_keyword[keyword]['VIEWS'])
        body_filled = body_filled.replace('$verified', result_by_keyword[keyword]['VERIFIED'])
        body_filled = body_filled.replace('$time', result_by_keyword[keyword]['TIME'])
        body_str += body_filled

    return html.replace('$body', body_str)
