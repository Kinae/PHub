html = '<html><head><style>div.block{display: inline-block;}div.gallery{margin:5px;border:1px solid ' \
       '#ccc;float:left;width:220px}div.gallery:hover {border:1px solid #777}div.gallery img{' \
       'width:100%;height:auto}div.desc{color: white; padding: 10px;text-align:center;overflow: hidden;white-space: ' \
       'nowrap;text-overflow: ellipsis; margin: 0px; height: 15px; font-size: small}div.container{' \
       'position:relative}div.text-block-bottom-left{' \
       'font-size:14px;position:absolute;bottom:0;left:0; background-color:transparent;color:white;padding-left:0px; ' \
       'padding-bottom:0px}div.text-block-bottom-right{' \
       'font-size:14px;position:absolute;bottom:0;right:0;background-color:transparent;color:white;padding-right:0px' \
       '}div.text-block-top-left{font-size:14px;position:absolute;top:0;left:0; ' \
       'background-color:transparent;color:white;padding-left:2px}div.text-block-top-right{' \
       'font-size:14px;position:absolute;top:0;right:0;background-color:transparent;color:white;padding-right:2px}h1' \
       '.text-h1{color: white;}p.text-video{margin-bottom: inherit; padding: 4px}body {background-color: ' \
       'black}</style></head><body>$block</body></html> '

block = '<div class="block"><h1 class="text-h1">$keyword</h1>$gallery</div> '

gallery = '<div class="gallery"><a target="_blank" href="$href"><div class="container"><img src="$img" width="300" ' \
          'height="200"><div class="text-block-bottom-right"><p class="text-video">$quality $duration</p></div><div ' \
          'class="text-block-bottom-left"><p class="text-video">$vote</p></div></div></a><div ' \
          'class="desc">$title</div></div> '


def build(block_str):
    return html.replace('$block', block_str)


def construct_block(keyword_str, gallery_str):
    return block.replace('$keyword', keyword_str).replace('$gallery', gallery_str)


def construct_gallery(result):
    return gallery.replace('$href', 'https://fr.pornhub.com/view_video.php?viewkey=' + result['VIDEO_KEY']) \
        .replace('$img', result['IMAGE']) \
        .replace('$duration', result['DURATION']) \
        .replace('$quality', result['QUALITY']) \
        .replace('$title', result['TITLE']) \
        .replace('$vote', result['VOTE'])
