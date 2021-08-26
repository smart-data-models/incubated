originalSource = """
isc:ds1 a qb:DataSet ;
    qb:structure isc:dsd1 ;
    rdfs:label "Population 15 and over by sex, age and activity status"@en , "Population de 15 ans ou plus par sexe, âge et type d'activité"@fr ;
    sdmx-attribute:unitMeasure <urn:sdmx:org.sdmx.infomodel.codelist.Code=ESTAT:CL_UNIT(1.2).PS> .

isc:obs-Y15-19-1-01001 a qb:Observation ;
    qb:dataSet isc:ds1 ;
    isc:dim-age isc:age-Y15-19 ;
    isc:dim-sex isc:sex-1 ;
    isc:dim-lau isc:lau-01001 ;
    isc:att-nuts3 isc:nuts3-FRK21 ;
    sdmx-measure:obsValue "116.3"^^xsd:float .

# (Observations for all other French LAUs)

isc:obs-Y_GE100-2-97617 a qb:Observation ;
    qb:dataSet isc:ds1 ;
    isc:dim-age isc:age-Y_GE100;
    isc:dim-sex isc:sex-2 ;
    isc:dim-lau isc:lau-97617 ;
    isc:att-nuts3 isc:nuts3-FRY50 ;
    sdmx-measure:obsValue "37.1"^^xsd:float .

isc:obs-Y15-19-1-001001 a qb:Observation ;
    qb:dataSet isc:ds1 ;
    isc:dim-age isc:age-Y15-19;
    isc:dim-sex isc:sex-1 ;
    isc:dim-lau isc:lau-001001 ;
    isc:att-nuts3 isc:nuts3-ITC11 ;
    sdmx-measure:obsValue "72.8"^^xsd:float .

# (Observations for all other Italian LAUs)

isc:obs-Y15-19-1-111107 a qb:Observation ;
    qb:dataSet isc:ds1 ;
    isc:dim-age isc:age-Y_GE100;
    isc:dim-sex isc:sex-2 ;
    isc:dim-lau isc:lau-111107 ;
    isc:att-nuts3 isc:nuts3-ITG2H ;
    sdmx-measure:obsValue "132.0"^^xsd:float ."""

payloadJson = {
    "dataset"
}