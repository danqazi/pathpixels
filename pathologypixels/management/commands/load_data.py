from viewer.models import Diagnosis
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        Diagnosis.objects.all().delete()
        diagnoses = derm.split('\n')
        for diagnosis in diagnoses:
            text = diagnosis.strip()
            print(text)
            if not text:
                continue
            diagnosis = Diagnosis.objects.filter(text=text).first()
            if diagnosis:
                continue
            Diagnosis.objects.create(text=text)


derm = """Blue nevus and cellular blue nevus
Nodular basal cell carcinoma
Superficial basal cell carcinoma
Micronodular basal cell carcinoma
Infiltrating basal cell carcinoma
Sclerosing/morphoeic basal cell carcinoma
Basosquamous carcinoma
Pigmented basal cell carcinoma
Basal cell carcinoma with adnexal differentiation
Fibroepithelial basal cell carcinoma
Squamous cell carcinoma
Keratoacanthoma
Acantholytic squamous cell carcinoma
Spindle cell squamous cell carcinoma
Verrucous squamous cell carcinoma
Adenosquamous carcinoma
Clear cell squamous cell carcinoma
Merkel cell carcinoma
Actinic keratosis
Arsenical keratosis
PUVA keratosis
Verruca vulgaris
Verruca plantaris
Verruca plana
Seborrhoeic keratosis
Solar lentigo
Lichen planus–like keratosis
Clear cell acanthoma
Warty dyskeratoma
Low-CSD melanoma (superficial spreading melanoma)
Simple lentigo and lentiginous melanocytic naevus
Junctional nevus
Compound nevus
Dermal nevus
Dysplastic nevus
Nevus spilus
Halo nevus
Meyerson nevus
Recurrent nevus
Deep penetrating nevus
Melanocytoma
Pigmented epithelioid melanocytoma
Lentigo maligna melanoma
Desmoplastic melanoma
Malignant Spitz tumour (Spitz melanoma)
Spitz naevus
Pigmented spindle cell nevus (Reed nevus)
Acral melanoma
Acral nevus
Mucosal melanoma (genital, oral, sinonasal)
Genital nevus
Melanoma arising in blue nevus
Mongolian spot
Nevus of Ito and nevus of Ota
Melanoma arising in giant congenital nevus
Congenital melanocytic nevus
Uveal melanoma
Conjunctival melanoma
Conjunctival melanocytic intraepithelial neoplasia/ primary acquired melanosis
Conjunctival nevus
Nodular melanoma
Nevoid melanoma
Metastatic melanoma
Adnexal adenocarcinoma not otherwise specified
Microcystic adnexal carcinoma
Porocarcinoma
Malignant mixed tumor
Hidradenocarcinoma
Mucinous carcinoma
Endocrine mucin-producing sweat gland carcinoma
Digital papillary adenocarcinoma
Adenoid cystic carcinoma
Apocrine carcinoma
Squamoid eccrine ductal carcinoma
Syringocystadenocarcinoma papilliferum
Secretory carcinoma
Cribriform carcinoma
Signet-ring cell/histiocytoid carcinoma
Hidrocystoma/cystadenoma
Syringofibroadenoma
Cutaneous manifestations of chronic active EBV infection
Blastic plasmacytoid dendritic cell neoplasm
Spindle cell/pleomorphic lipoma
Collagenous fibroma
Rapidly involuting congenital hemangioma
Syringoma
Poroma
Hidradenoma
Spiradenoma
Cylindroma
Tubular adenoma
Mixed tumor
Myoepithelioma
Pilomatrical carcinoma
Proliferating trichilemmal tumour
Trichoblastic carcinoma/carcinosarcoma
Trichilemmal carcinoma
Trichoblastoma
Pilomatricoma
Trichofolliculoma
Pilar sheath acanthoma
Melanocytic matricoma
Spindle cell–predominant trichodiscoma
Sebaceous carcinoma
Sebaceous adenoma
Sebaceoma
Mammary Paget disease
Extramammary Paget disease
Adenocarcinoma of anogenital mammary-like glands
Hidradenoma papilliferum
Mycosis fungoides
Folliculotropic mycosis fungoides
Granulomatous slack skin
Pagetoid reticulosis
Sezary syndrome
Extranodal NK/T-cell lymphoma, nasal type
Primary cutaneous gamma-delta T-cell lymphoma
Primary cutaneous CD8+ aggressive epidermotropic cytotoxic T-cell lymphoma
Primary cutaneous acral CD8+ T-cell lymphoma
Primary cutaneous CD4+ small/medium T-cell lymphoproliferative disorder
Systemic anaplastic large cell lymphoma
Angioimmunoblastic T-cell lymphoma
T-cell prolymphocytic leukaemia
Primary cutaneous marginal zone (MALT) lymphoma
Primary cutaneous follicle centre lymphoma
Primary cutaneous diffuse large B-cell lymphoma, leg type
Intravascular large B-cell lymphoma
EBV-positive mucocutaneous ulcer
Lymphomatoid granulomatosis
Mantle cell lymphoma
Burkitt lymphoma
Chronic lymphocytic leukemia/small lymphocytic lymphoma
T-lymphoblastic and B-lymphoblastic leukemia/lymphoma
Cutaneous involvement in myeloid leukemia
Cutaneous mastocytosis
Langerhans cell histiocytosis
Indeterminate cell histiocytosis/indeterminate dendritic cell tumor
Rosai–Dorfman disease
Juvenile xanthogranuloma
Erdheim–Chester disease
Reticulohistiocytosis
Atypical lipomatous tumor
Pleomorphic liposarcoma
Lipoma
Angiolipoma
Nevus lipomatosus superficialis
Myxoinflammatory fibroblastic sarcoma
Dermatofibrosarcoma protuberans
Plexiform fibrohistiocytic tumour
Superficial fibromatosis
Dermatofibroma (fibrous histiocytoma)
Epithelioid fibrous histiocytoma
Fibroma
Calcifying aponeurotic fibroma
Sclerotic fibroma
Nuchal-type fibroma
Gardner fibroma
Pleomorphic fibroma
Elastofibroma
Superficial acral fibromyxoma
Cutaneous myxoma
Dermatomyofibroma
Myofibroma
Plaque-like CD34+ dermal fibroma
Nodular fasciitis
Cutaneous leiomyomas
Glomus tumor
Myopericytoma
Angioleiomyoma
Cutaneous angiosarcoma
Composite haemangioendothelioma
Kaposiform haemangioendothelioma
Pseudomyogenic haemangioendothelioma
Retiform haemangioendothelioma
Epithelioid haemangioendothelioma
Kaposi sarcoma
Atypical vascular lesion
Cherry hemangioma
Sinusoidal hemangioma
Microvenular hemangioma
Hobnail hemangioma
Glomeruloid hemangioma
Spindle cell hemangioma
Epithelioid hemangioma
Tufted hemangioma
Angiokeratoma
Basal cell carcinoma with sarcomatoid differentiation
Squamous cell carcinoma in situ (Bowen disease)
Large cell acanthoma
Special-site nevi (of the breast, axilla, scalp, and ear)
Combined nevus, including combined BAP1-inactivated nevus/melanocytoma
Proliferative nodules in congenital melanocytic nevus
Malignant neoplasms arising from spiradenoma, cylindroma, or spiradenocylindroma
Syringocystadenoma papilliferum
Trichilemmoma
Tumour of the follicular infundibulum
Fibroadenoma and phyllodes tumor of anogenital mammary-like glands
Lymphomatoid papulosis
Primary cutaneous anaplastic large cell lymphoma
Subcutaneous panniculitis-like T-cell lymphoma
Fibroma of tendon sheath
Myofibromatosis
Cutaneous leiomyosarcoma (atypical smooth muscle tumor)
Cutaneous epithelioid angiomatous nodule
Infantile hemangioma
Non-involuting congenital hemangioma
Lobular capillary hemangioma
Verrucous venous malformation
Arteriovenous malformation
Lymphangioma (superficial lymphatic malformation)
Neurofibroma
Solitary circumscribed neuroma
Dermal nerve sheath myxoma
Dermal nerve sheath myxoma
Granular cell tumor
Granular cell tumor
Malignant peripheral nerve sheath tumor
Atypical fibroxanthoma
Pleomorphic dermal sarcoma
Pleomorphic dermal sarcoma
Epithelioid sarcoma
Dermal clear cell sarcoma
Ewing sarcoma
Primitive non-neural granular cell tumor
Cellular neurothekeoma
Familial melanoma
Xeroderma pigmentosum
Nevoid basal cell carcinoma syndrome (Gorlin syndrome)
Carney complex
BAP1 tumor predisposition syndrome
Muir–Torre syndrome
Cutaneous adult T-cell leukemia/lymphoma"""