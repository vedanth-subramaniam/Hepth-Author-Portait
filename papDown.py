import arxiv
import urllib.request
import PyPDF2


dataset = pd.read_c
search = arxiv.Search(id_list=["hep-th/9910110"])

for result in search.results():
    print('Title: ', result.title, '\nDate: ',result.published , '\nId: ', result.entry_id, '\nSummary: ',result.summary ,'\nURL: ', result.pdf_url, '\n\n')
    urllib.request.urlretrieve(result.pdf_url + '.pdf', "filename.pdf")


pdffileobj=open('filename.pdf','rb')