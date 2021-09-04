# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CombinedSynonyms(models.Model):
    hgnc_id = models.TextField(db_column='HGNC_ID', blank=True, null=True)  # Field name made lowercase.
    symbol = models.TextField(db_column='Symbol', blank=True, null=True)  # Field name made lowercase.
    synonym = models.TextField(db_column='Synonym', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COMBINED_synonyms'


class DgidbCategories(models.Model):
    hgnc_id = models.TextField(db_column='HGNC_ID', blank=True, null=True)  # Field name made lowercase.
    gene_symbol = models.TextField(db_column='Gene_Symbol', blank=True, null=True)  # Field name made lowercase.
    gene_name = models.TextField(db_column='Gene_Name', blank=True, null=True)  # Field name made lowercase.
    category = models.TextField(blank=True, null=True)
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_date = models.IntegerField(db_column='Source_Date', blank=True, null=True)  # Field name made lowercase.
    download_date = models.IntegerField(db_column='Download_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DGIdb_categories'


class DrugbankTargets(models.Model):
    drugbank_id = models.TextField(db_column='DrugBank_ID', blank=True, null=True)  # Field name made lowercase.
    hgnc_id = models.TextField(db_column='HGNC_ID', blank=True, null=True)  # Field name made lowercase.
    uniprot_id = models.TextField(db_column='Uniprot_ID', blank=True, null=True)  # Field name made lowercase.
    drug_name = models.TextField(db_column='Drug_Name', blank=True, null=True)  # Field name made lowercase.
    target = models.TextField(db_column='Target', blank=True, null=True)  # Field name made lowercase.
    actions = models.TextField(db_column='Actions', blank=True, null=True)  # Field name made lowercase.
    genesymbol = models.TextField(db_column='GeneSymbol', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_date = models.IntegerField(db_column='Source_Date', blank=True, null=True)  # Field name made lowercase.
    download_date = models.IntegerField(db_column='Download_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DRUGBANK_Targets'


class DrugbankDrugInfo(models.Model):
    drugbank_id = models.TextField(db_column='DrugBank_ID', blank=True, null=True)  # Field name made lowercase.
    accession_numbers = models.TextField(db_column='Accession_Numbers', blank=True, null=True)  # Field name made lowercase.
    common_name = models.TextField(db_column='Common_name', blank=True, null=True)  # Field name made lowercase.
    synonyms = models.TextField(db_column='Synonyms', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DRUGBANK_drug_info'


class GoBiologicalProcesses(models.Model):
    hgnc_id = models.TextField(db_column='HGNC_ID', blank=True, null=True)  # Field name made lowercase.
    gene_symbol = models.TextField(db_column='Gene_symbol', blank=True, null=True)  # Field name made lowercase.
    biological_process = models.TextField(db_column='Biological_Process', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_date = models.IntegerField(db_column='Source_Date', blank=True, null=True)  # Field name made lowercase.
    download_date = models.IntegerField(db_column='Download_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GO_biological_processes'


class GoCellularComponent(models.Model):
    hgnc_id = models.TextField(db_column='HGNC_ID', blank=True, null=True)  # Field name made lowercase.
    cellular_component = models.TextField(db_column='Cellular_component', blank=True, null=True)  # Field name made lowercase.
    gene_symbol = models.TextField(db_column='Gene_symbol', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_date = models.IntegerField(db_column='Source_Date', blank=True, null=True)  # Field name made lowercase.
    download_date = models.IntegerField(db_column='Download_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GO_cellular_component'


class GoMolecularFunction(models.Model):
    hgnc_id = models.TextField(db_column='HGNC_ID', blank=True, null=True)  # Field name made lowercase.
    molecular_function = models.TextField(db_column='Molecular_Function', blank=True, null=True)  # Field name made lowercase.
    gene_symbol = models.TextField(db_column='Gene_Symbol', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_date = models.IntegerField(db_column='Source_Date', blank=True, null=True)  # Field name made lowercase.
    download_date = models.IntegerField(db_column='Download_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GO_molecular_function'


class HgncGeneInfo(models.Model):
    hgnc_id = models.TextField(db_column='HGNC_ID', blank=True, primary_key=True)  # Field name made lowercase.
    gene_symbol = models.TextField(db_column='Gene_symbol', blank=True, null=True)  # Field name made lowercase.
    approved_name = models.TextField(db_column='Approved_name', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    previous_symbols = models.TextField(db_column='Previous_symbols', blank=True, null=True)  # Field name made lowercase.
    alias_symbols = models.TextField(db_column='Alias_symbols', blank=True, null=True)  # Field name made lowercase.
    chromosome = models.TextField(db_column='Chromosome', blank=True, null=True)  # Field name made lowercase.
    accession_numbers = models.TextField(db_column='Accession_numbers', blank=True, null=True)  # Field name made lowercase.
    ensembl_id = models.TextField(db_column='Ensembl_ID', blank=True, null=True)  # Field name made lowercase.
    ncbi_id = models.IntegerField(db_column='NCBI_ID', blank=True, null=True)  # Field name made lowercase.
    uniprot_id = models.TextField(db_column='UniProt_ID', blank=True, null=True)  # Field name made lowercase.
    omim_id = models.TextField(db_column='OMIM_ID', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_date = models.IntegerField(db_column='Source_Date', blank=True, null=True)  # Field name made lowercase.
    download_date = models.IntegerField(db_column='Download_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HGNC_gene_info'


class HippieProteinInteractions(models.Model):
    hgnc_id_1 = models.TextField(db_column='HGNC_ID_1', blank=True, null=True)  # Field name made lowercase.
    gene_symbol_1 = models.TextField(db_column='Gene_Symbol_1', blank=True, null=True)  # Field name made lowercase.
    gene_id_1 = models.IntegerField(db_column='Gene_ID_1', blank=True, null=True)  # Field name made lowercase.
    hgnc_id_2 = models.TextField(db_column='HGNC_ID_2', blank=True, null=True)  # Field name made lowercase.
    gene_symbol_2 = models.TextField(db_column='Gene_Symbol_2', blank=True, null=True)  # Field name made lowercase.
    gene_id_2 = models.IntegerField(db_column='Gene_ID_2', blank=True, null=True)  # Field name made lowercase.
    score = models.FloatField(db_column='Score', blank=True, null=True)  # Field name made lowercase.
    experiments = models.TextField(db_column='Experiments', blank=True, null=True)  # Field name made lowercase.
    pmids = models.TextField(db_column='PMIDS', blank=True, null=True)  # Field name made lowercase.
    sources = models.TextField(db_column='Sources', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HIPPIE_protein_interactions'


class HpaBiologicalProcess(models.Model):
    hgnc_id = models.TextField(db_column='HGNC_ID', blank=True, null=True)  # Field name made lowercase.
    gene = models.TextField(db_column='Gene', blank=True, null=True)  # Field name made lowercase.
    biological_process = models.TextField(db_column='Biological_process', blank=True, null=True)  # Field name made lowercase.
    field4 = models.TextField(blank=True, null=True)
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_date = models.IntegerField(db_column='Source_Date', blank=True, null=True)  # Field name made lowercase.
    download_date = models.IntegerField(db_column='Download_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HPA_biological_process'


class HpaMolecularFunction(models.Model):
    hgnc_id = models.TextField(db_column='HGNC_ID', blank=True, null=True)  # Field name made lowercase.
    gene = models.TextField(db_column='Gene', blank=True, null=True)  # Field name made lowercase.
    molecular_function = models.TextField(db_column='Molecular_function', blank=True, null=True)  # Field name made lowercase.
    field4 = models.TextField(blank=True, null=True)
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_date = models.IntegerField(db_column='Source_Date', blank=True, null=True)  # Field name made lowercase.
    download_date = models.IntegerField(db_column='Download_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HPA_molecular_function'


class HpaProteinClasses(models.Model):
    hgnc_id = models.TextField(db_column='HGNC_ID', blank=True, null=True)  # Field name made lowercase.
    gene = models.TextField(db_column='Gene', blank=True, null=True)  # Field name made lowercase.
    protein_class = models.TextField(db_column='Protein_class', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_date = models.IntegerField(db_column='Source_Date', blank=True, null=True)  # Field name made lowercase.
    download_date = models.IntegerField(db_column='Download_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HPA_protein_classes'


class HpaProteinSubcellularLocations(models.Model):
    hgnc_id = models.TextField(db_column='HGNC_ID', blank=True, null=True)  # Field name made lowercase.
    gene = models.TextField(db_column='Gene', blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.TextField(db_column='Subcellular_location', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_date = models.IntegerField(db_column='Source_Date', blank=True, null=True)  # Field name made lowercase.
    download_date = models.IntegerField(db_column='Download_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HPA_protein_subcellular_locations'


class HpoGenesToPhenotype(models.Model):
    hgnc_id = models.TextField(db_column='HGNC_ID', blank=True, null=True)  # Field name made lowercase.
    entrez_gene_id = models.IntegerField(blank=True, null=True)
    gene_symbol = models.TextField(blank=True, null=True)
    hpo_term_id = models.TextField(db_column='HPO_Term_ID', blank=True, null=True)  # Field name made lowercase.
    hpo_term_name = models.TextField(db_column='HPO_Term_Name', blank=True, null=True)  # Field name made lowercase.
    disease_id_for_link = models.TextField(db_column='disease_ID_for_link', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_date = models.IntegerField(db_column='Source_date', blank=True, null=True)  # Field name made lowercase.
    download_date = models.IntegerField(db_column='Download_date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HPO_genes_to_phenotype'


class MsigdbPathways(models.Model):
    hgnc_id = models.TextField(db_column='HGNC_ID', blank=True, null=True)  # Field name made lowercase.
    pathway = models.TextField(db_column='Pathway', blank=True, null=True)  # Field name made lowercase.
    url = models.TextField(db_column='URL', blank=True, null=True)  # Field name made lowercase.
    gene_symbol = models.TextField(db_column='gene_symbol', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_date = models.IntegerField(db_column='Source_Date', blank=True, null=True)  # Field name made lowercase.
    download_date = models.IntegerField(db_column='Download_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MSigDB_pathways'


class NcbiGeneInfo(models.Model):
    hgncid = models.TextField(db_column='HGNCID', blank=True, null=True)  # Field name made lowercase.
    geneid = models.IntegerField(db_column='GeneID', blank=True, null=True)  # Field name made lowercase.
    symbol = models.TextField(db_column='Symbol', blank=True, null=True)  # Field name made lowercase.
    synonyms = models.TextField(db_column='Synonyms', blank=True, null=True)  # Field name made lowercase.
    dbxrefs = models.TextField(db_column='dbXrefs', blank=True, null=True)  # Field name made lowercase.
    chromosome = models.TextField(blank=True, null=True)
    map_location = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    type_of_gene = models.TextField(blank=True, null=True)
    symbol_from_nomenclature_authority = models.TextField(db_column='Symbol_from_nomenclature_authority', blank=True, null=True)  # Field name made lowercase.
    full_name_from_nomenclature_authority = models.TextField(db_column='Full_name_from_nomenclature_authority', blank=True, null=True)  # Field name made lowercase.
    other_designations = models.TextField(db_column='Other_designations', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_date = models.IntegerField(db_column='Source_date', blank=True, null=True)  # Field name made lowercase.
    download_date = models.IntegerField(db_column='Download_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NCBI_gene_info'


class NcbiGenesToPhenotypes(models.Model):
    hgnc_id = models.TextField(db_column='HGNC_ID', blank=True, null=True)  # Field name made lowercase.
    ncbi_id = models.IntegerField(db_column='NCBI_ID', blank=True, null=True)  # Field name made lowercase.
    gene_symbol = models.TextField(db_column='Gene_Symbol', blank=True, null=True)  # Field name made lowercase.
    condition = models.TextField(db_column='Condition', blank=True, null=True)  # Field name made lowercase.
    concept_id = models.TextField(db_column='Concept_ID', blank=True, null=True)  # Field name made lowercase.
    omim_id = models.IntegerField(db_column='OMIM_ID', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_date = models.IntegerField(db_column='Source_Date', blank=True, null=True)  # Field name made lowercase.
    download_date = models.IntegerField(db_column='Download_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NCBI_genes_to_phenotypes'


class SnapDrugTargets(models.Model):
    hgnc_id = models.TextField(db_column='HGNC_ID', blank=True, null=True)  # Field name made lowercase.
    drugbank_id = models.TextField(db_column='DrugBank_ID', blank=True, null=True)  # Field name made lowercase.
    uniprot_id = models.TextField(db_column='UniProt_ID', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_date = models.IntegerField(db_column='Source_Date', blank=True, null=True)  # Field name made lowercase.
    download_date = models.IntegerField(db_column='Download_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SNAP_drug_targets'


class StringProteinInteractions(models.Model):
    hgnc_1 = models.TextField(db_column='HGNC_1', blank=True, null=True)  # Field name made lowercase.
    hgnc_2 = models.TextField(db_column='HGNC_2', blank=True, null=True)  # Field name made lowercase.
    combined_score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'STRING_protein_interactions'

class vwProteinInteractions(models.Model):
    geneSymbol1 = models.TextField(db_column='GeneSymbol1', primary_key=True)
    geneName1 = models.TextField(db_column='GeneName1')
    geneSymbol2 = models.TextField(db_column='GeneSymbol2')
    geneName2 = models.TextField(db_column='GeneName2')
    hippie_score = models.TextField(db_column='hippiescore')
    string_score = models.IntegerField(db_column='stringscore')
    experiments = models.TextField(db_column='Experiments')
    pmids = models.TextField(db_column='PMIDs')
    in_vivo_in_vitro = models.TextField(db_column='InVivoInVitro')
    source = models.TextField(db_column='Source')

    class Meta:
        managed = False
        db_table = 'vw_ProteinInteractions'

class vwDrugTargets(models.Model):
    hgnc_id = models.TextField(db_column='HGNC_ID', primary_key=True)
    gene_symbol = models.TextField(db_column='gene_symbol')
    drugbank_id = models.TextField(db_column='Drugbank_ID')
    drug_name = models.TextField(db_column='common_name')
    actions = models.TextField(db_column='actions')
    synonyms = models.TextField(db_column='synonyms')
    brand_names = models.TextField(db_column='brand_names')
    source = models.TextField(db_column='Source')

    class Meta:
        managed = False
        db_table = 'vw_DrugTargets'

class vwDiseases(models.Model):
    hgnc_id = models.TextField(db_column='HGNC_ID', primary_key=True)
    gene_symbol = models.TextField(db_column='gene_symbol')
    disease_name = models.TextField(db_column='condition')
    concept_id = models.TextField(db_column='concept_id')
    disease_id = models.TextField(db_column='disease_id')
    source = models.TextField(db_column='Source')

    class Meta:
        managed = False
        db_table = 'vw_Diseases'

class vwGeneInfo(models.Model):
    gene_symbol = models.TextField(db_column='gene_symbol')
    approved_name = models.TextField(db_column='approved_name')
    synonyms = models.TextField(db_column='synonyms')
    protein_class = models.TextField(db_column='protein_class')
    categories = models.TextField(db_column='categories')
    chromosome = models.TextField(db_column='chromosome')
    hgnc_id = models.TextField(db_column='HGNC_ID', primary_key=True)
    entrez_id = models.TextField(db_column='entrez_id')
    ensembl_id = models.TextField(db_column='ensembl_id')
    uniprot_id = models.TextField(db_column='uniprot_id')
    druggable = models.TextField(db_column='druggable')
    enzyme = models.TextField(db_column='enzyme')
    kinase = models.TextField(db_column='kinase')
    transcription_factor = models.TextField(db_column='transcriptionFactor')
    secreted = models.TextField(db_column='secreted')
    transmembrane = models.TextField(db_column='transmembrane')

    class Meta:
        managed = False
        db_table = 'vw_GeneInfo'
