import gzip
import requests
import io
from contextlib import closing

def get_archive(url):
    """
    Returns decoded string obtained at `url`
    """
    print("GA: Gathering archive '{}' from\n    {}\n    ...".format(url.split('/')[-1], '/'.join(url.split('/')[:-1])))
    raw = requests.get(url)
    print("GA: Done.\n")
    with closing(raw), gzip.GzipFile(fileobj=io.BytesIO(raw.content)) as archive:
        return bytes(archive.read()).decode()
    return 'Requests error'


def show_dict(dict:dict):
    """
    Gets dictionary and returns its content as a string.
    """
    content = ''
    for item in dict.items():
        content += "{}:\t{}\n".format(item[0], item[1])
    return content


def test():
    ar = get_archive('http://hgdownload.soe.ucsc.edu/goldenPath/hg38/chromosomes/chrY.fa.gz')
    print("Fist 1000 chars in\nhttp://hgdownload.soe.ucsc.edu/goldenPath/hg38/chromosomes/chrY.fa.gz\n{}".format(ar[:1000]))

if __name__ == '__main__':
    test()