Covid Vaccination Demographic Analysis
================
Victoria Puck-Karam

# Front Matter

``` r
library(tidyverse)
```

    ## ── Attaching packages ─────────────────────────────────────── tidyverse 1.3.1 ──

    ## ✓ ggplot2 3.3.5     ✓ purrr   0.3.4
    ## ✓ tibble  3.1.6     ✓ dplyr   1.0.7
    ## ✓ tidyr   1.1.4     ✓ stringr 1.4.0
    ## ✓ readr   2.1.1     ✓ forcats 0.5.1

    ## ── Conflicts ────────────────────────────────────────── tidyverse_conflicts() ──
    ## x dplyr::filter() masks stats::filter()
    ## x dplyr::lag()    masks stats::lag()

``` r
library(mosaic)
```

    ## Registered S3 method overwritten by 'mosaic':
    ##   method                           from   
    ##   fortify.SpatialPolygonsDataFrame ggplot2

    ## 
    ## The 'mosaic' package masks several functions from core packages in order to add 
    ## additional features.  The original behavior of these functions should not be affected by this.

    ## 
    ## Attaching package: 'mosaic'

    ## The following object is masked from 'package:Matrix':
    ## 
    ##     mean

    ## The following objects are masked from 'package:dplyr':
    ## 
    ##     count, do, tally

    ## The following object is masked from 'package:purrr':
    ## 
    ##     cross

    ## The following object is masked from 'package:ggplot2':
    ## 
    ##     stat

    ## The following objects are masked from 'package:stats':
    ## 
    ##     binom.test, cor, cor.test, cov, fivenum, IQR, median, prop.test,
    ##     quantile, sd, t.test, var

    ## The following objects are masked from 'package:base':
    ## 
    ##     max, mean, min, prod, range, sample, sum

``` r
library( lubridate )
```

    ## 
    ## Attaching package: 'lubridate'

    ## The following objects are masked from 'package:base':
    ## 
    ##     date, intersect, setdiff, union

``` r
library('scales')
```

    ## 
    ## Attaching package: 'scales'

    ## The following object is masked from 'package:mosaic':
    ## 
    ##     rescale

    ## The following object is masked from 'package:purrr':
    ## 
    ##     discard

    ## The following object is masked from 'package:readr':
    ## 
    ##     col_factor

## Guiding Question: How do demographic factors (race, median income, % healthcare employment, etc.) impact the percentage of citizens recieving the covid vaccine, by state?

### Why is This Important?

Covid-19 has plagued our society for nearly 3 years at this point. My
generation, specifically, has faced severe mental health repercussions
and the entire human population has faced severe sickness and difficult
life circumstances. Needless to say, COVID has made everyone’s lives
difficult but luckily a vaccine has been developed successfully. Despot
the vaccine being scientifically proven to be safe and effective, only
65% of Americans are fully vaccinated. In order to achieve herd
immunity, the US and the world needs to have over an 80% vaccination
rate. It is essential that we understand trends in vaccination rates
based on geographical location in the US and demographic factors, in
order to assemble systems to combat the anti-vaxx narative in those
communities.

### Preparing Primary Data Source

#### Citation:

Urban Institute. 2021. Vaccinating the US. Accessible from [this
website](https://datacatalog.urban.org/dataset/vaccinating-us). Data
originally sourced from Centers for Disease Control, 5 year American
Community Survey (2015-2019) and Bureau of Labor Statistics, developed
at the Urban Institute, and made available under the ODC-BY 1.0
Attribution License.

#### secondary dataset from [CDC covid dashboard](https://covid.cdc.gov/covid-data-tracker/COVIDData/getAjaxData?id=vaccination_data)

``` r
StateVax <- read.csv("/Users/victoriapuck-karam/Documents/Covid-Vaccination-Demographics-Analysis/CDCStateVax.csv")
StateDemography <- read_csv("/Users/victoriapuck-karam/Documents/Covid-Vaccination-Demographics-Analysis/CDCStateData.csv")
```

    ## Rows: 52 Columns: 8

    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (1): NAME
    ## dbl (7): medincome, medincome_moe, total_population, total_employment_educat...

    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
CovidState <- read.csv("/Users/victoriapuck-karam/Documents/Covid-Vaccination-Demographics-Analysis/CDC Daily Vaccination Data - state_timeseries.csv")


glimpse(StateVax)
```

    ## Rows: 3,216
    ## Columns: 6
    ## $ GEOID    <int> 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 2…
    ## $ NAME     <chr> "Mississippi", "Mississippi", "Mississippi", "Mississippi", "…
    ## $ value    <int> 2976149, 2876039, 100110, 1758081, 1678232, 79849, 1124559, 1…
    ## $ AGEGROUP <chr> "All ages", "All ages", "All ages", "All ages", "All ages", "…
    ## $ RACE     <chr> "All races", "All races", "All races", "White alone", "White …
    ## $ HISP     <chr> "Both Hispanic Origins", "Non-Hispanic", "Hispanic", "Both Hi…

``` r
glimpse(CovidState)
```

    ## Rows: 16,768
    ## Columns: 14
    ## $ date                                <chr> "2021-01-12", "2021-01-13", "2021-…
    ## $ location                            <chr> "Alabama", "Alabama", "Alabama", "…
    ## $ daily_vaccinations_raw              <int> NA, 5906, 8260, 8267, NA, NA, NA, …
    ## $ daily_vaccinations                  <int> NA, 5906, 7083, 7478, 7498, 7509, …
    ## $ total_vaccinations                  <int> 78134, 84040, 92300, 100567, NA, N…
    ## $ total_distributed                   <int> 377025, 378975, 435350, 444650, NA…
    ## $ people_vaccinated                   <int> 70861, 74792, 80480, 86956, NA, NA…
    ## $ people_fully_vaccinated_per_hundred <dbl> 0.15, 0.19, NA, 0.28, NA, NA, NA, …
    ## $ total_vaccinations_per_hundred      <dbl> 1.59, 1.71, 1.88, 2.05, NA, NA, NA…
    ## $ people_fully_vaccinated             <int> 7270, 9245, NA, 13488, NA, NA, NA,…
    ## $ people_vaccinated_per_hundred       <dbl> 1.45, 1.53, 1.64, 1.77, NA, NA, NA…
    ## $ distributed_per_hundred             <dbl> 7.69, 7.73, 8.88, 9.07, NA, NA, NA…
    ## $ daily_vaccinations_per_million      <int> NA, 1205, 1445, 1525, 1529, 1531, …
    ## $ share_doses_used                    <dbl> 0.207, 0.222, 0.212, 0.226, NA, NA…

``` r
glimpse(StateDemography)
```

    ## Rows: 52
    ## Columns: 8
    ## $ NAME                          <chr> "Alaska", "Alabama", "Arkansas", "Arizon…
    ## $ medincome                     <dbl> 76715, 48486, 45726, 56213, 71228, 68811…
    ## $ medincome_moe                 <dbl> 894, 364, 350, 275, 217, 364, 552, 1081,…
    ## $ total_population              <dbl> 737438, 4887871, 3013825, 7171646, 39557…
    ## $ total_employment_education    <dbl> 31290, 165470, 107580, 245130, 1520420, …
    ## $ total_employment_healthcare   <dbl> 48930, 261380, 187730, 391830, 2515020, …
    ## $ percent_education_employment  <dbl> 0.04243069, 0.03385319, 0.03569550, 0.03…
    ## $ percent_healthcare_employment <dbl> 0.06635134, 0.05347523, 0.06228962, 0.05…

## Data Wrangling

#### joining demographic data to vaccination data by state name

``` r
StateVaxDemo <-
  StateVax%>%
  inner_join(StateDemography,by = "NAME" )

glimpse(StateVaxDemo)
```

    ## Rows: 3,216
    ## Columns: 13
    ## $ GEOID                         <int> 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, …
    ## $ NAME                          <chr> "Mississippi", "Mississippi", "Mississip…
    ## $ value                         <int> 2976149, 2876039, 100110, 1758081, 16782…
    ## $ AGEGROUP                      <chr> "All ages", "All ages", "All ages", "All…
    ## $ RACE                          <chr> "All races", "All races", "All races", "…
    ## $ HISP                          <chr> "Both Hispanic Origins", "Non-Hispanic",…
    ## $ medincome                     <dbl> 43567, 43567, 43567, 43567, 43567, 43567…
    ## $ medincome_moe                 <dbl> 395, 395, 395, 395, 395, 395, 395, 395, …
    ## $ total_population              <dbl> 2986530, 2986530, 2986530, 2986530, 2986…
    ## $ total_employment_education    <dbl> 111420, 111420, 111420, 111420, 111420, …
    ## $ total_employment_healthcare   <dbl> 163030, 163030, 163030, 163030, 163030, …
    ## $ percent_education_employment  <dbl> 0.03730751, 0.03730751, 0.03730751, 0.03…
    ## $ percent_healthcare_employment <dbl> 0.05458844, 0.05458844, 0.05458844, 0.05…

#### converting all decimal values into percentages, and whole numbers of sub categories into percentages in order to standardize information

``` r
StateVaxPerc<- 
  StateVaxDemo%>%
  mutate(percentageOfPop= percent(value/total_population))%>%
  mutate(percent_education_employment=percent(percent_education_employment))%>%
  mutate(percent_healthcare_employment=percent(percent_healthcare_employment))%>%
  select(NAME,AGEGROUP,RACE,HISP,medincome,medincome_moe,percent_education_employment,percent_healthcare_employment,percentageOfPop)


glimpse(StateVaxPerc)
```

    ## Rows: 3,216
    ## Columns: 9
    ## $ NAME                          <chr> "Mississippi", "Mississippi", "Mississip…
    ## $ AGEGROUP                      <chr> "All ages", "All ages", "All ages", "All…
    ## $ RACE                          <chr> "All races", "All races", "All races", "…
    ## $ HISP                          <chr> "Both Hispanic Origins", "Non-Hispanic",…
    ## $ medincome                     <dbl> 43567, 43567, 43567, 43567, 43567, 43567…
    ## $ medincome_moe                 <dbl> 395, 395, 395, 395, 395, 395, 395, 395, …
    ## $ percent_education_employment  <chr> "3.7308%", "3.7308%", "3.7308%", "3.7308…
    ## $ percent_healthcare_employment <chr> "5.45884%", "5.45884%", "5.45884%", "5.4…
    ## $ percentageOfPop               <chr> "99.652405969%", "96.300355262%", "3.352…

#### Cleaned the percentage data of the percent symbols for easier mathematical operations

``` r
StateVaxPerc<-
  StateVaxPerc %>% 
  mutate(percentageOfPop = gsub(pattern = "[, %]", replacement = "", percentageOfPop),percent_healthcare_employment = gsub(pattern = "[, %]", replacement = "", percent_healthcare_employment),percent_education_employment = gsub(pattern = "[, %]", replacement = "", percent_education_employment))

head(StateVaxPerc)
```

    ##          NAME AGEGROUP        RACE                  HISP medincome
    ## 1 Mississippi All ages   All races Both Hispanic Origins     43567
    ## 2 Mississippi All ages   All races          Non-Hispanic     43567
    ## 3 Mississippi All ages   All races              Hispanic     43567
    ## 4 Mississippi All ages White alone Both Hispanic Origins     43567
    ## 5 Mississippi All ages White alone          Non-Hispanic     43567
    ## 6 Mississippi All ages White alone              Hispanic     43567
    ##   medincome_moe percent_education_employment percent_healthcare_employment
    ## 1           395                       3.7308                       5.45884
    ## 2           395                       3.7308                       5.45884
    ## 3           395                       3.7308                       5.45884
    ## 4           395                       3.7308                       5.45884
    ## 5           395                       3.7308                       5.45884
    ## 6           395                       3.7308                       5.45884
    ##   percentageOfPop
    ## 1    99.652405969
    ## 2    96.300355262
    ## 3     3.352050708
    ## 4    58.867012888
    ## 5    56.193374920
    ## 6     2.673637968

### the relationships between the percentageOfPop is that they should add up the the total of all races which are around 100% example: Both Hispanic origins Mississippi make up 99.652405969% of the whole population which is essentially 100%, the Non-Hispanic population makes up 96.300355262% and Hispanic makes up 3.352050708% of the population.

#### Now to add the vaccination data to the demography data

``` r
  CovidState%>%
  group_by(location)%>%
  summarise(date=max(date)) ### based on this information, we can see that the most recent day that the information was updated was 2021-09-30, so I will be using this data 
```

    ## # A tibble: 64 × 2
    ##    location          date      
    ##    <chr>             <chr>     
    ##  1 Alabama           2021-09-30
    ##  2 Alaska            2021-09-30
    ##  3 American Samoa    2021-09-30
    ##  4 Arizona           2021-09-30
    ##  5 Arkansas          2021-09-30
    ##  6 Bureau of Prisons 2021-09-30
    ##  7 California        2021-09-30
    ##  8 Colorado          2021-09-30
    ##  9 Connecticut       2021-09-30
    ## 10 Delaware          2021-09-30
    ## # … with 54 more rows

``` r
head(CovidState)
```

    ##         date location daily_vaccinations_raw daily_vaccinations
    ## 1 2021-01-12  Alabama                     NA                 NA
    ## 2 2021-01-13  Alabama                   5906               5906
    ## 3 2021-01-14  Alabama                   8260               7083
    ## 4 2021-01-15  Alabama                   8267               7478
    ## 5 2021-01-16  Alabama                     NA               7498
    ## 6 2021-01-17  Alabama                     NA               7509
    ##   total_vaccinations total_distributed people_vaccinated
    ## 1              78134            377025             70861
    ## 2              84040            378975             74792
    ## 3              92300            435350             80480
    ## 4             100567            444650             86956
    ## 5                 NA                NA                NA
    ## 6                 NA                NA                NA
    ##   people_fully_vaccinated_per_hundred total_vaccinations_per_hundred
    ## 1                                0.15                           1.59
    ## 2                                0.19                           1.71
    ## 3                                  NA                           1.88
    ## 4                                0.28                           2.05
    ## 5                                  NA                             NA
    ## 6                                  NA                             NA
    ##   people_fully_vaccinated people_vaccinated_per_hundred distributed_per_hundred
    ## 1                    7270                          1.45                    7.69
    ## 2                    9245                          1.53                    7.73
    ## 3                      NA                          1.64                    8.88
    ## 4                   13488                          1.77                    9.07
    ## 5                      NA                            NA                      NA
    ## 6                      NA                            NA                      NA
    ##   daily_vaccinations_per_million share_doses_used
    ## 1                             NA            0.207
    ## 2                           1205            0.222
    ## 3                           1445            0.212
    ## 4                           1525            0.226
    ## 5                           1529               NA
    ## 6                           1531               NA

### the most recently dated information about vaccination status is 2021-09-03 , so select each unqiue case at this time to analyze most recent data

``` r
MostRecentData <-
  CovidState%>%
  rename("NAME"='location')%>%
  filter(date=="2021-09-30")%>%
  select(NAME,total_vaccinations,people_fully_vaccinated_per_hundred,people_fully_vaccinated)

head(MostRecentData)
```

    ##                NAME total_vaccinations people_fully_vaccinated_per_hundred
    ## 1           Alabama            4532608                               42.62
    ## 2            Alaska             792368                               50.59
    ## 3    American Samoa              62048                               51.06
    ## 4           Arizona            8214287                               51.09
    ## 5          Arkansas            3018302                               45.59
    ## 6 Bureau of Prisons             227890                                  NA
    ##   people_fully_vaccinated
    ## 1                 2089852
    ## 2                  370114
    ## 3                   28433
    ## 4                 3718393
    ## 5                 1375964
    ## 6                  116661

### adding more demographic data by state

``` r
DemoVaxTogether<- 
  StateVaxPerc%>%
  inner_join(MostRecentData,by= "NAME")

head(DemoVaxTogether)
```

    ##          NAME AGEGROUP        RACE                  HISP medincome
    ## 1 Mississippi All ages   All races Both Hispanic Origins     43567
    ## 2 Mississippi All ages   All races          Non-Hispanic     43567
    ## 3 Mississippi All ages   All races              Hispanic     43567
    ## 4 Mississippi All ages White alone Both Hispanic Origins     43567
    ## 5 Mississippi All ages White alone          Non-Hispanic     43567
    ## 6 Mississippi All ages White alone              Hispanic     43567
    ##   medincome_moe percent_education_employment percent_healthcare_employment
    ## 1           395                       3.7308                       5.45884
    ## 2           395                       3.7308                       5.45884
    ## 3           395                       3.7308                       5.45884
    ## 4           395                       3.7308                       5.45884
    ## 5           395                       3.7308                       5.45884
    ## 6           395                       3.7308                       5.45884
    ##   percentageOfPop total_vaccinations people_fully_vaccinated_per_hundred
    ## 1    99.652405969            2783784                               43.51
    ## 2    96.300355262            2783784                               43.51
    ## 3     3.352050708            2783784                               43.51
    ## 4    58.867012888            2783784                               43.51
    ## 5    56.193374920            2783784                               43.51
    ## 6     2.673637968            2783784                               43.51
    ##   people_fully_vaccinated
    ## 1                 1294972
    ## 2                 1294972
    ## 3                 1294972
    ## 4                 1294972
    ## 5                 1294972
    ## 6                 1294972

### The first demographic feature of interest is the impact of race on overall state vaccination percentage

``` r
raceSpecificData<-
  DemoVaxTogether%>%
  mutate(rank =rank(people_fully_vaccinated_per_hundred))%>%
  arrange(desc(rank))
  
head(raceSpecificData)
```

    ##          NAME          AGEGROUP      RACE                  HISP medincome
    ## 1 Puerto Rico          All ages All races Both Hispanic Origins     20166
    ## 2 Puerto Rico 65 years and over All races Both Hispanic Origins     20166
    ## 3 Puerto Rico 18 years and over All races Both Hispanic Origins     20166
    ## 4     Vermont          All ages All races Both Hispanic Origins     60076
    ## 5     Vermont          All ages All races          Non-Hispanic     60076
    ## 6     Vermont          All ages All races              Hispanic     60076
    ##   medincome_moe percent_education_employment percent_healthcare_employment
    ## 1           190                       2.7614                       2.61396
    ## 2           190                       2.7614                       2.61396
    ## 3           190                       2.7614                       2.61396
    ## 4           656                       6.0179                       8.44644
    ## 5           656                       6.0179                       8.44644
    ## 6           656                       6.0179                       8.44644
    ##   percentageOfPop total_vaccinations people_fully_vaccinated_per_hundred
    ## 1    99.954337085            4673227                               70.30
    ## 2    21.271469629            4673227                               70.30
    ## 3    82.029342570            4673227                               70.30
    ## 4    99.631166583             897919                               69.48
    ## 5    97.600347438             897919                               69.48
    ## 6     2.030819145             897919                               69.48
    ##   people_fully_vaccinated rank
    ## 1                 2245195 3152
    ## 2                 2245195 3152
    ## 3                 2245195 3152
    ## 4                  433565 3119
    ## 5                  433565 3119
    ## 6                  433565 3119

### percentages of each race breakdown disregarding age and hispanic origin breakdown

``` r
raceSpecificData<-
  raceSpecificData%>%
  pivot_wider(names_from = RACE,values_from =percentageOfPop  )%>%
  filter(AGEGROUP ==    'All ages' )%>%
  filter(HISP =="Both Hispanic Origins")%>%
  select(NAME,"people_fully_vaccinated_per_hundred","White alone","American Indian and Alaska Native alone","Black alone","Asian alone","Native Hawaiian and Other Pacific Islander alone","Two or more races")%>%
  rename("white"= "White alone")%>%
  mutate(white= as.numeric(white))%>%
  mutate()

head(raceSpecificData)
```

    ## # A tibble: 6 × 8
    ##   NAME   people_fully_vacc… white `American Indian … `Black alone` `Asian alone`
    ##   <chr>               <dbl> <dbl> <chr>              <chr>         <chr>        
    ## 1 Puert…               70.3  NA   <NA>               <NA>          <NA>         
    ## 2 Vermo…               69.5  93.9 0.389749944        1.400928311   1.910269695  
    ## 3 Conne…               68.7  79.5 0.575676701        <NA>          4.942500906  
    ## 4 Maine                68.5  94.8 0.729749762        1.695377479   1.301550205  
    ## 5 Rhode…               68.3  83.8 1.083215503        8.522341970   3.739282995  
    ## 6 Massa…               67.9  80.5 0.497091558        9.010266223   7.208146332  
    ## # … with 2 more variables:
    ## #   Native Hawaiian and Other Pacific Islander alone <chr>,
    ## #   Two or more races <chr>

## Correlation between percent of white people versus the vaccination rate in that state

``` r
ggplot(raceSpecificData, aes(x=people_fully_vaccinated_per_hundred))+geom_point(aes(y=white), alpha=3,stroke=0.5, color="orange")+geom_smooth(aes(x=people_fully_vaccinated_per_hundred, y=white),color='purple')+theme_classic()+xlab("vaccination rate")+ylab("percentage of white citizens")+ggtitle("            % of white citizens versus vaccination rate per state")
```

    ## `geom_smooth()` using method = 'loess' and formula 'y ~ x'

    ## Warning: Removed 1 rows containing non-finite values (stat_smooth).

    ## Warning: Removed 1 rows containing missing values (geom_point).

![](covidDemoAnalysis_files/figure-gfm/unnamed-chunk-11-1.png)<!-- -->
## Correlation between percent of white people versus the vaccination
rate in that state I wanted to analyze this relation as white people
face reap all the advantages of society, especially in regards to
familial wealth and healthcare systems that are tailored towards them. I
hypothesized that the areas with the highest vaccination rates would
have the highest percentage of white people, because historically they
have been given a reason to distrust the american health care system.

According to this graphic there doesn’t seem to be a strong correlation
between the percentage of white citizens versus the vaccination rate.
This could be explained by the fact that white people are the majority
in America, so there is more variation from state to state about
vaccination status that prevents an obvious trend from being observed.

## More generally a correlation between percentage of residents who are minorities racially

``` r
minorityData<- 
  raceSpecificData%>%
  mutate(minorities= 100- white)%>% # find the non-white percentage of citizens
  select(NAME, people_fully_vaccinated_per_hundred,minorities )
minorityData
```

    ## # A tibble: 51 × 3
    ##    NAME          people_fully_vaccinated_per_hundred minorities
    ##    <chr>                                       <dbl>      <dbl>
    ##  1 Puerto Rico                                  70.3      NA   
    ##  2 Vermont                                      69.5       6.10
    ##  3 Connecticut                                  68.7      20.5 
    ##  4 Maine                                        68.5       5.16
    ##  5 Rhode Island                                 68.3      16.2 
    ##  6 Massachusetts                                67.9      19.5 
    ##  7 New Jersey                                   64.3      28.3 
    ##  8 Maryland                                     64.1      41.4 
    ##  9 New Mexico                                   63.2      18.1 
    ## 10 New Hampshire                                61.5       6.66
    ## # … with 41 more rows

``` r
ggplot(minorityData, aes(x=minorities))+geom_jitter(aes(y=people_fully_vaccinated_per_hundred))+geom_smooth(aes(y=people_fully_vaccinated_per_hundred))+xlab("percent of minorities")+ylab("vaccination rate")+theme_classic()+ggtitle("            % of racial minority citizens versus vaccination rate per state")
```

    ## `geom_smooth()` using method = 'loess' and formula 'y ~ x'

    ## Warning: Removed 1 rows containing non-finite values (stat_smooth).

    ## Warning: Removed 1 rows containing missing values (geom_point).

![](covidDemoAnalysis_files/figure-gfm/unnamed-chunk-13-1.png)<!-- -->

This chart seems to demonstrate a stronger correlation between the the
rate of citizens that are minorities and vaccination rate than the rate
of white citizens and vaccination rate. The confidence is not high
enough to draw a strong conclusion, but it appears that in general the
states with lower percentages of minority citizens have the highest
vaccination rates. There doesn’t seem to be a strong enough correlation
to determine if race has a strong influence on vaccination rates.

## geographic location versus vaccination rate

``` r
mUSMap(DemoVaxTogether,key= 'NAME', fill= 'people_fully_vaccinated_per_hundred')+ggtitle("Vaccination Rate By State ")
```

    ## Mapping API still under development and may change in future releases.

![](covidDemoAnalysis_files/figure-gfm/unnamed-chunk-14-1.png)<!-- -->

This map seems to reveal the strongest correlation between geographic
feature versus vaccination rate. The concentration of the lowest rates
is primarily located in the South. Something could be said as to the
correlation between the majority polilitcal affiliation of a state
versus vaccination rate, as that cluster of southern states has
historically voted red.

## Comparison Between State Vaccination Rate versus Income Across States:

### Visual Representation of weath accross states,

The map below represents the variation in median income per state. It
appears that most of the lower median income states are concentrated in
the south, much like the US map which maps the vaccination rates. There
seems to be visually a strong correlation between the two, so let’s
investigate that.

``` r
MedPerState<- 
  StateVaxDemo%>%
 select(NAME,medincome)%>%
  unique()

mUSMap(MedPerState,key= 'NAME', fill= 'medincome')
```

    ## Mapping API still under development and may change in future releases.

![](covidDemoAnalysis_files/figure-gfm/unnamed-chunk-15-1.png)<!-- -->

### data wrangled to pull only the vaccination data and the median income per state

``` r
medIncomeVersusVax<-
  DemoVaxTogether%>%
  select(NAME, people_fully_vaccinated_per_hundred, medincome)%>%
  group_by(NAME, people_fully_vaccinated_per_hundred, medincome)%>%
  unique()

medIncomeVersusVax
```

    ## # A tibble: 51 × 3
    ## # Groups:   NAME, people_fully_vaccinated_per_hundred, medincome [51]
    ##    NAME           people_fully_vaccinated_per_hundred medincome
    ##    <chr>                                        <dbl>     <dbl>
    ##  1 Mississippi                                   43.5     43567
    ##  2 Missouri                                      47.9     53560
    ##  3 Montana                                       48.5     52559
    ##  4 Nebraska                                      54.7     59116
    ##  5 Nevada                                        50.8     57598
    ##  6 New Hampshire                                 61.5     74057
    ##  7 New Jersey                                    64.3     79363
    ##  8 New Mexico                                    63.2     48059
    ##  9 North Carolina                                49.8     52413
    ## 10 North Dakota                                  44.2     63473
    ## # … with 41 more rows

``` r
ggplot(medIncomeVersusVax, aes(x= people_fully_vaccinated_per_hundred))+geom_point(aes(y= medincome))+geom_smooth(method=lm, aes(y=medincome ))+xlab("vaccination %")+ylab("median income")+ggtitle("              vaccination rate versus median income")
```

    ## `geom_smooth()` using formula 'y ~ x'

![](covidDemoAnalysis_files/figure-gfm/unnamed-chunk-17-1.png)<!-- -->
There is a very strong correlation between median income and vaccination
percentage. There is a very obvious relationship as income increases,
vaccination rate increases. As observed earlier, there is a connection
between access to health care and income, and then in turn the
vaccination rate.

## Conclusion:

In conclusion, the strongest demographic relationship observed from this
data set is the relationship between median income and vaccination rate.
Surprisingly, there was no obvious or strong relationships between any
of the racial demographic elements. In terms

**note: there were no strong relationships that could be observed using
three variables, which is why i chose to stay with 2 variable
comparisons**
