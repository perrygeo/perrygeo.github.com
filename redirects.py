"""
Dumb hack to generate a list of redirects from old wordpress urls
to new jekyll urls
"""
import glob

print "["
for post in glob.glob('_posts/*.markdown'):
    parts = post.split('-')
    dir = '/'.join(parts[:3]).replace('_posts/','')
    file = '-'.join(parts[3:]).replace('.markdown','')
    url = "/%s/%s/" % (dir, file)
    with open(post, 'r') as fh:
        for line in fh.readlines():
            if line.startswith('wpid'):
                wpid = int(line.replace('wpid:','').replace("'", '').strip())
    old = "/wordpress/?p=%d" % wpid
         
    print "('%s', '%s')," % (old, url)

print "]"
