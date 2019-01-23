# Bioinformatic_RNAseq_20190123

###record Chlamydomonas reinhardtii RNA_seq analysis procedure
#First--quality control and filter: raw data -> clean data  (need softwares containing FastP or combination of FastQC and Trimmomatic)

#second--alignment(reference, but no reference need transcriptome assembled de novo by Trinity): downloading reference genome  from Phytozome website, and then aligning  clean data to reference genome (softwares: STAR, attention
:u should create genome index before alignment; hisat2; subread; bowtie2, and so on)

#third--expression quatification: need second procedure result file like .BAM file, get genes level  or transcripts level reads count (
software: featureCounts), other key points: Samples similarity detection, method: PCA analysis(scikit-learn ) and relation analysis (scipy)

#fourth--differential genes analysis: hunting for differential genes at comprision between control group and test group (software: 
edger ; DEseq2)

#fifth and more--enrichment including GO and KEGG analysis and more(GO enrichment analysis: need TopGO or GOstat ,and clusterprofile, the last
 two softwares can also  be available on Kegg enrichment anaysis)

#others--more details analysis: WGCNA analysis (need phenotype data or metabolomics data); GSEA analysis ; specials genes relationship analysis
genes category anaysis
