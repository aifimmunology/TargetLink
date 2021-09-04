from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse
from django.http import JsonResponse

from search.models import vwGeneInfo, vwDrugTargets, vwDiseases, vwProteinInteractions, MsigdbPathways

def index(request):
    # print("genelist:", genelist)
    search_terms = request.GET.get("search_terms")
    print(request.GET)

    genelist = []
    if search_terms != None:
        gene_symbols = search_terms.upper().split('\r\n')
        for gene_symbol in gene_symbols:
            match = vwGeneInfo.objects.filter(gene_symbol = gene_symbol)
            if len(match) == 1:
                search_result = SearchResult(match[0])
                genelist.append(search_result)

    context = { 'search_terms': search_terms, 'genelist': genelist }

    return render(request, 'search/index.html', context)

def gene_details(request):
    symbol = request.GET.get('gene_symbol')
    data = {
        'drug_targets': list(vwDrugTargets.objects.filter(gene_symbol = symbol).values()),
        'diseases': list(vwDiseases.objects.filter(gene_symbol = symbol).values()),
        'protein_interactions': list(vwProteinInteractions.objects.filter(geneSymbol1 = symbol).values()),
        'pathways': list(MsigdbPathways.objects.filter(gene_symbol = symbol).values())
    }

    return JsonResponse(data)


class SearchResult:

    hgnc_id = None
    gene_symbol = None
    gene_info = None
    drug_targets = None
    diseases = None
    protein_interactions = None

    def __init__(self, gene_info_record):
        self.hgnc_id = gene_info_record.hgnc_id
        self.gene_symbol = gene_info_record.gene_symbol
        self.gene_info = gene_info_record
        # self.drug_targets = vwDrugTargets.objects.filter(gene_symbol = self.gene_symbol)
        # self.diseases = vwDiseases.objects.filter(gene_symbol = self.gene_symbol)
        # self.protein_interactions = vwProteinInteractions.objects.filter(geneSymbol1 = self.gene_symbol)