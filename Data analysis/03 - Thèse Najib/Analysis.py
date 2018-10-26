
# coding: utf-8

# In[7]:


import pandas as pd
from scipy import stats

file = 'Base de Données thèse NK VF.xlsx'
xlsx = pd.ExcelFile(file)
df = xlsx.parse(dtype="category")
df = df.set_index('Numéro Patient')

df[["Âge au moment de l'accident(ans)", "Délai entre la prise en charge initiale et la reconstruction (jours)", "Recul jusqu'au questionnaire (ans)", "Durée d'hospitalisaiton initiale (Semaines)", "Nombre de Chirurgie", "PF", "RP", "RE", "BP", "VT", "MH", "SF", "GH", "PCS", "MCS"]] = df[["Âge au moment de l'accident(ans)", "Délai entre la prise en charge initiale et la reconstruction (jours)", "Recul jusqu'au questionnaire (ans)", "Durée d'hospitalisaiton initiale (Semaines)", "Nombre de Chirurgie", "PF", "RP", "RE", "BP", "VT", "MH", "SF", "GH", "PCS", "MCS"]].apply(pd.to_numeric)

dfRec = df[df['Catégorie'] == 0]
dfRec = dfRec.drop(['Catégorie', "Délai par rapport à l'accident 2 (jours)", "Délai par rapport au premier lambeau (J)", "Indication 2", "Gestes effectués avant la reconstruction.1", "Bilan angiographique avant la reconstruction.1", "Type du Lambeau 2", "Artère 2", "Anastomose 2", "Pontage", "Gestes associés.1", "Greffe oseuse", "Prélèvements bactériologiques osseux réalisés.1", "Complicaitions immédiates", "Reprise Précoce", "Résultats.1", "Résultats de la Biopsie osseuse.1", "Repise Tardive"], axis = 1)
dfAmp = df[df['Catégorie'] == 1]
dfAmp = dfAmp[['Sexe', "Âge au moment de l'accident(ans)", "Type D'accident", "Site de la fracture", "Type de Fracture", "PDS cutanée initiale", "Lésion vasculaire initiale", "Lésion Neurologique initiale", "Recul jusqu'au questionnaire (ans)", "Durée d'hospitalisaiton initiale (Semaines)", "Nombre de Chirurgie", "Douleur Chronique", "Appareillage", "Marche avec Appareillage", "Périmètre de Marche", "Conduite Véhicule", "Vie professionnelle", "Escaliers", "Station Debout pendant 1h", "Courir", "Sautiller", "PF", "RP", "RE", "BP", "VT", "MH", "SF", "GH", "PCS", "MCS"]]

dfRecDesc = dfRec.describe(include = "all").transpose()
dfRecDesc['IQR'] = dfRecDesc['75%'] - dfRecDesc['25%']
dfAmpDesc = dfAmp.describe(include = "all").transpose()
dfAmpDesc['IQR'] = dfAmpDesc['75%'] - dfAmpDesc['25%']

newdfcomp = xlsx.parse(dtype="float")
newdfcompqual = newdfcomp[["Catégorie", "Sexe", "Type D'accident", "Type de Fracture", "PDS cutanée initiale", "Lésion vasculaire initiale", "Lésion Neurologique initiale", "Douleur Chronique", "Appareillage", "Marche avec Appareillage", "Périmètre de Marche", "Conduite Véhicule", "Vie professionnelle", "Escaliers", "Station Debout pendant 1h", "Courir", "Sautiller"]]
newdfcompquant = newdfcomp[["Âge au moment de l'accident(ans)", "Recul jusqu'au questionnaire (ans)", "Durée d'hospitalisaiton initiale (Semaines)", "Nombre de Chirurgie", "PF", "RP", "RE", "BP", "VT", "MH", "SF", "GH", "PCS", "MCS"]]

ttest_normality = newdfcompquant[newdfcompquant.columns[0:]].apply(lambda x: stats.shapiro(x)[1])
ttest_equal_var = newdfcompquant[newdfcompquant.columns[0:]].apply(lambda x: stats.levene(x.head(13), x.tail(11))[1])
ttest_student_pvalue = newdfcompquant[newdfcompquant.columns[0:]].apply(lambda x: stats.ttest_ind(x.head(13), x.tail(11))[1])
ttest_mannwhitney_stat = newdfcompquant[newdfcompquant.columns[0:]].apply(lambda x: stats.mannwhitneyu(x.head(13), x.tail(11))[0])
ttest_mannwhitney_pvalue = newdfcompquant[newdfcompquant.columns[0:]].apply(lambda x: stats.mannwhitneyu(x.head(13), x.tail(11))[1])
rownames = list(newdfcompquant)

comparative = pd.DataFrame( index= rownames)
comparative['test de normalité (shapiro)'] = ttest_normality.round(6)
comparative['test de variance égale (levene)'] = ttest_equal_var
comparative['mann Whithney U statistic'] = ttest_mannwhitney_stat
comparative['mann Whithney U pvalue'] = ttest_mannwhitney_pvalue.round(6)
comparative['student pvalue'] = ttest_student_pvalue.round(6)

analysis = pd.ExcelWriter('descriptive_comparative.xlsx')
dfRecDesc.to_excel(analysis,'Reconstruction description')
dfRec.corr(method='pearson').to_excel(analysis, 'Reconstruction correlation')
dfAmpDesc.to_excel(analysis,'Amputation description')
dfAmp.corr(method='pearson').to_excel(analysis, 'Amputation correlation')
comparative.to_excel(analysis, 'étude comparative quantitative')

comparative


# In[8]:


ct1 = pd.crosstab(df['Catégorie'], df['Sexe'])
ct2 = pd.crosstab(df['Catégorie'], df["Type D'accident"])
ct3 = pd.crosstab(df['Catégorie'], df["Type de Fracture"])
ct4 = pd.crosstab(df['Catégorie'], df["PDS cutanée initiale"])
ct5 = pd.crosstab(df['Catégorie'], df["Lésion vasculaire initiale"])
ct6 = pd.crosstab(df['Catégorie'], df["Lésion Neurologique initiale"])
ct7 = pd.crosstab(df['Catégorie'], df["Douleur Chronique"])
ct8 = pd.crosstab(df['Catégorie'], df["Appareillage"])
ct9 = pd.crosstab(df['Catégorie'], df["Marche avec Appareillage"])
ct10 = pd.crosstab(df['Catégorie'], df["Périmètre de Marche"])
ct11 = pd.crosstab(df['Catégorie'], df["Conduite Véhicule"])
ct12 = pd.crosstab(df['Catégorie'], df["Vie professionnelle"])
ct13 = pd.crosstab(df['Catégorie'], df["Escaliers"])
ct14 = pd.crosstab(df['Catégorie'], df["Station Debout pendant 1h"])
ct15 = pd.crosstab(df['Catégorie'], df["Courir"])
ct16 = pd.crosstab(df['Catégorie'], df["Sautiller"])

cs1 = stats.chi2_contingency(ct1)
cs2 = stats.chi2_contingency(ct2)
cs3 = stats.chi2_contingency(ct3)
cs4 = stats.chi2_contingency(ct4)
cs5 = stats.chi2_contingency(ct5)
cs6 = stats.chi2_contingency(ct6)
cs7 = stats.chi2_contingency(ct7)
cs8 = stats.chi2_contingency(ct8)
cs9 = stats.chi2_contingency(ct9)
cs10 = stats.chi2_contingency(ct10)
cs11 = stats.chi2_contingency(ct11)
cs12 = stats.chi2_contingency(ct12)
cs13 = stats.chi2_contingency(ct13)
cs14 = stats.chi2_contingency(ct14)
cs15 = stats.chi2_contingency(ct15)
cs16 = stats.chi2_contingency(ct16)

statistic = [cs1[0], cs2[0], cs3[0], cs4[0], cs5[0], cs6[0], cs7[0], cs8[0], cs9[0], cs10[0], cs11[0], cs12[0], cs13[0], cs14[0], cs15[0], cs16[0]]
pvalue = [cs1[1], cs2[1], cs3[1], cs4[1], cs5[1], cs6[1], cs7[1], cs8[1], cs9[1], cs10[1], cs11[1], cs12[1], cs13[1], cs14[1], cs15[1], cs16[1]]
degree_of_freedom = [cs1[2], cs2[2], cs3[2], cs4[2], cs5[2], cs6[2], cs7[2], cs8[2], cs9[2], cs10[2], cs11[2], cs12[2], cs13[2], cs14[2], cs15[2], cs16[2]]
rownames2 = ["Sexe", "Type D'accident", "Type de Fracture", "PDS cutanée initiale", "Lésion vasculaire initiale", "Lésion Neurologique initiale", "Douleur Chronique", "Appareillage", "Marche avec Appareillage", "Périmètre de Marche", "Conduite Véhicule", "Vie professionnelle", "Escaliers", "Station Debout pendant 1h", "Courir", "Sautiller"]


comparative2 = pd.DataFrame( index= rownames2)
comparative2['Chi-squared stat'] = statistic
comparative2['Chi-squared pvalue'] = pvalue
comparative2['Chi-squared degree of freedom'] = degree_of_freedom

comparative2.to_excel(analysis, 'étude comparative qualitative')

comparative2


# In[15]:


import pandas as pd
from scipy import stats

file = 'Base de Données thèse NK VF sheet2.xlsx'
xlsx = pd.ExcelFile(file)
df2 = pd.read_excel(xlsx, 'Feuil2', dtype="category")
df2 = df2.set_index('Numéro Patient')
df2 = df2.dropna()

ct17 = pd.crosstab(df2['Catégorie'], df2['Infecté'])
cs17 = stats.chi2_contingency(ct17)


ttest3stat = cs17[0]
ttest3pval = cs17[1]
ttest3degree = cs17[2]
rownames = list(df2)

comparative3 = pd.DataFrame( index= rownames)
comparative3['statistic'] = ttest3stat
comparative3['pvalue'] = ttest3pval
comparative3['degree of freedom'] = ttest3degree
comparative3.to_excel(analysis, 'étude comparative qual. suite')

analysis.save()

comparative3

