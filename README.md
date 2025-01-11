# DIRECTIVE FOR RUNNING THE PROJECT

All the packages use during the implementation are listed in the requirement.txt in the backend folder with their
corresponding version. Since virtual environments can go beyond lot of GB of data, the venv of the project is not pushed into Github and a virtual env. need to be created and the packages need to be installed inside.

---

##### CREATION OF VIRTUAL ENVIRONMENT AND PACKAGE INSTALLATION (windows)

#### 1. Navigate to the backend directory and create a virtual environnement

    - cd coderr_backend
    - python -m venv ["name of the virtual env"] (for Windows users)
    - python3 -m venv ["name of the virtual env"] (for MAC or Linux users)
    e.x. : python -m venv env

#### 2. activation of the created environnement

    - .\env\Scripts\activate and press ENTER    (for Windows users)
    - source env/bin/activate and press ENTER (for MAC or Linux users)

#### 3. Install the packages from requirements.txt

    - pip install -r requirements.txt

Now we need to create a DB with the models define in all apps inside the project
Please notice that a project need to be structured in different apps for simplicity and re-usability.

#### 1. Creation of DB and migration

    - python manage.py makemigrations coderr_basic_infos_app coderr_order_offer_app coderr_user_profile_app coderr_auth_app
    - python manage.py migrate

#### START OF THE DEVELOPMENT SERVER

    - python manage.py runserver

## API Dokumentation (From Developer Akadmie GmbH)

- DokumentationBackend-EndpunkteCoderr......................................................................
  - DokumentationfürdieBackend-EndpunktezuAngeboten..............................................................
    - Übersicht.............................................................................................................................................................
    - Endpunkte...........................................................................................................................................................
    - 1.GET/offers/...................................................................................................................................................
      - Beschreibung:....................................................................................................................................
      - Anfragemethoden:..........................................................................................................................
      - Query-Parameter:............................................................................................................................
      - BeispielfüreineAnfrage:.............................................................................................................
    - 2.POST/offers/................................................................................................................................................
      - Beschreibung:....................................................................................................................................
      - Anfragemethoden:..........................................................................................................................
      - Anfrage-Body(Beispiel):..............................................................................................................
    - 3.GET/offers/{id}/.........................................................................................................................................
      - Beschreibung:....................................................................................................................................
      - Anfragemethoden:..........................................................................................................................
      - URL-Parameter:.................................................................................................................................
      - BeispielfüreineAnfrage:.............................................................................................................
    - 4.PATCH/offers/{id}/................................................................................................................................
      - Beschreibung:..................................................................................................................................
      - Anfragemethoden:........................................................................................................................
      - URL-Parameter:..............................................................................................................................
      - Anfrage-Body(BeispielfürPATCH):...................................................................................
    - 5.DELETE/offers/{id}/................................................................................................................................
      - Beschreibung:...................................................................................................................................
      - Anfragemethoden:.........................................................................................................................
      - URL-Parameter:...............................................................................................................................
      - BeispielfüreineAnfrage:............................................................................................................
      - Antwort(beiErfolg)Hinweis,dasistnicht“204NoContent”:...............................
    - 6.GET/offerdetails/{id}/............................................................................................................................
      - Beschreibung:...................................................................................................................................
      - Anfragemethoden:.........................................................................................................................
      - URL-Parameter:...............................................................................................................................
      - BeispielfüreineAnfrage:............................................................................................................
    - 7.AllgemeinePermissions:........................................................................................
  - DokumentationfürdieBackend-EndpunktezuBestellungen........................................................
  - API-Endpunkte................................................................................................................................................
  - EndpunkteimDetail.....................................................................................................................................
  - 1.GET/orders/.................................................................................................................................................
    - Beschreibung:..................................................................................................................................
    - Anfragemethoden:........................................................................................................................
    - Antwort(Beispiel):.........................................................................................................................
    - Query-Parameter:..........................................................................................................................
    - Hinweis:...............................................................................................................................................
  - 2.POST/orders/.............................................................................................................................................
    - Beschreibung:..................................................................................................................................
    - Anfragemethoden:........................................................................................................................
    - Anfrage-Body(Beispiel):............................................................................................................
    - Hinweis:..............................................................................................................................................
  - 3.GET/orders/{id}/......................................................................................................................................
    - Beschreibung:..................................................................................................................................
    - Anfragemethoden:........................................................................................................................
    - URL-Parameter:..............................................................................................................................
    - BeispielfüreineAnfrage:...........................................................................................................
  - 4.PATCH/orders/{id}/...............................................................................................................................
    - Beschreibung:..................................................................................................................................
    - Anfragemethoden:........................................................................................................................
    - URL-Parameter:..............................................................................................................................
    - Anfrage-Body(Beispiel):............................................................................................................
    - Hinweis:..............................................................................................................................................
  - 5.DELETE/orders/{id}/..............................................................................................................................
    - Beschreibung:..................................................................................................................................
    - Anfragemethoden:........................................................................................................................
    - URL-Parameter:...............................................................................................................................
    - BeispielfüreineAnfrage:...........................................................................................................
- ErweiterteAPIfürdasZählenvonBestellungen....................................................................................
  - API-Endpunkte................................................................................................................................................
  - EndpunkteimDetail.....................................................................................................................................
  - 1.GET/order-count/{business_user_id}/...........................................................................................
    - Beschreibung:..................................................................................................................................
    - Anfragemethoden:........................................................................................................................
    - URL-Parameter:...............................................................................................................................
    - BeispielfüreineAnfrage:...........................................................................................................
    - Fehlerfälle:.........................................................................................................................................
    - Hinweis:..............................................................................................................................................
  - 2.GET/completed-order-count/{business_user_id}/.................................................
    - Beschreibung:..................................................................................................................................
    - Anfragemethoden:........................................................................................................................
    - URL-Parameter:..............................................................................................................................
    - BeispielfüreineAnfrage:...........................................................................................................
    - Fehlerfälle:.........................................................................................................................................
    - Hinweis:..........................................................................................................
  - Zusammenfassung:......................................................................................................................................
- DokumentationdesAPI-EndpunktsfürBasisinformationen...........................................................
  - 1.GET/base-info/......................................................................................................
    - Beschreibung:..................................................................................................................................
    - Anfragemethoden:........................................................................................................................
    - URL-Parameter:...............................................................................................................................
    - BeispielfüreineAnfrage:...........................................................................................................
    - Felder:............................................................................................................
- API-EndpunktefürBenutzerprofile.............................................................................................................
  - 1.GET/profile/<int:pk>/.............................................................................................
    - Beschreibung:.................................................................................................
    - Anfragemethoden:..........................................................................................
    - URL-Parameter:.............................................................................................
  - 2.GET/profiles/business/..........................................................................................
    - Beschreibung:.................................................................................................
    - Anfragemethoden:..........................................................................................
    - BeispielfüreineAnfrage:...............................................................................
  - 3.GET/profiles/customer/..........................................................................................
    - Beschreibung:.................................................................................................
    - Anfragemethoden:..........................................................................................
    - BeispielfüreineAnfrage:...............................................................................
  - Zusammenfassung:......................................................................................................................................
- Authentifizierungs-undRegistrierungs-API...........................................................................................
  - 1.POST/login/...........................................................................................................
    - Beschreibung:.................................................................................................
    - Anfragemethoden:..........................................................................................
    - ErforderlicheFelder:.......................................................................................
    - Antwort:..........................................................................................................
  - 2.POST/registration/.................................................................................................
    - Beschreibung:.................................................................................................
    - Anfragemethoden:..........................................................................................
    - ErforderlicheFelder:.......................................................................................
    - Antwort:..........................................................................................................
    - Statuscodes:...................................................................................................
  - Zusammenfassung:.....................................................................................................................................
- APIFehlerstruktur:...........................................................................................................
  - 1.AllgemeinerFehleraufbau:.....................................................................................
  - 2.WennmehrereFelderFehlerhaben:.....................................................................
  - 3.AllgemeinerFehlerohnespezifischeFelder(z.B.Authentifizierungsfehler):.........

## DokumentationBackend-EndpunkteCoderr......................................................................

### DokumentationfürdieBackend-EndpunktezuAngeboten..............................................................

DieseDokumentationbeschreibtdieEndpunkte,umdieBackend-Funktionalität
passendzumFrontendzuentwickeln.DiefolgendeBeschreibungdecktdieStruktur
undFunktionalitätderAPI-Endpunkteab,basierendaufdendefiniertenViews,
ModellenundSerializern.

#### Übersicht.............................................................................................................................................................

DieAPIbietetfolgendeEndpunkte:

1. **GET/offers/** – ListeallerAngebote(Offers)mitFilter-und
   Suchmöglichkeiten.
2. **POST/offers/** – ErstelleneinesneuenAngebotsinklusivezugehöriger
   Details.
3. **GET/offers/{id}/** – AbrufenderDetailseinesspezifischenAngebots.
4. **PATCH/offers/{id}/** – AktualisiereneinesspezifischenAngebots.
5. **DELETE/offers/{id}/** – LöscheneinesspezifischenAngebotsUNDden
   zugehörigenAngebotsdetails.
6. **GET/offerdetails/{id}/** – AbrufenderDetailseinesspezifischen
   Angebotsdetails.

#### Endpunkte...........................................................................................................................................................

#### 1.GET/offers/...................................................................................................................................................

##### Beschreibung:....................................................................................................................................

DieserEndpunktgibteineListevonAngebotenzurück.JedesAngebotenthälteine
ÜbersichtderAngebotsdetails,denminimalenPreisunddiekürzesteLieferzeit.

##### Anfragemethoden:..........................................................................................................................

###### GET

##### Query-Parameter:............................................................................................................................

```
creator_id :FiltertdieAngebotenachdemBenutzer,dersieerstellthat.
min_price :FiltertAngebotemiteinemMindestpreis.
max_delivery_time :FiltertAngebote,derenLieferzeitkürzerodergleichdem
angegebenenWertist.
ordering :SortiertdieAngebotenachdenFeldern“updated_at”oder
”min_price”.
```

```
search :DurchsuchtdieFelder“title”und“description”nach
Übereinstimmungen.
page_size :Gibtan,wievieleErgebnisseproSeitezurückgegebenwerden
sollen.DiesistimFrontendinderconfig.jsdefiniert,bittesetzediepage_size
indeinerPaginationgenauaufdengleichenWert.DieserQuery-Parameter
wirdnichtdirektgenutzt.
```

**Paginierung** :DieAntwortvonGET/offers/istnachPageNumberPaginationpaginiert.

##### BeispielfüreineAnfrage:.............................................................................................................

GET/offers/?creator_id=1&min_price=50&ordering=min_price&search=Website

**Antwort:**
[
{
"id":1,
"user":1,
"title":"WebsiteDesign",
"image":null,
"description":"ProfessionellesWebsite-Design...",
"created_at":"2024-09-25T10:00:00Z",
"updated_at":"2024-09-28T12:00:00Z",
"details":[
{"id":1,"url":"/offerdetails/1/"},
{"id":2,"url":"/offerdetails/2/"},
{"id":3,"url":"/offerdetails/3/"}
],
"min_price":100.00,
"min_delivery_time":7,
"user_details":{
"first_name":"John",
"last_name":"Doe",
"username":"jdoe"
}
}
]

**2.POST/offers/**

**Beschreibung:**

DieserEndpunktermöglichtes,einneuesAngebot(Offer)zuerstellen,dasgenau
dreiAngebotsdetails(OfferDetail)enthaltenmuss.DieseDetailssolltendieTypen
basic,standardundpremiumabdecken.

**Validierung** :

BeimErstelleneinesAngebotsmüssengenaudreiDetailsangegebenwerden(und
auchjeweilseinmal der"offer_type":basic,standard,premium).

Außerdemsollteallesvorhandensein,außerein“image”.

Die"revisions"sindIntegerundfangenbei-1an(die-1istder“unendlich
Revisionen”-Fall).

Die"delivery_time_in_days"sindnurpositiveInteger.

EssolltemindestenseinFeaturedrinsein.

##### Anfragemethoden:..........................................................................................................................

###### POST

##### Anfrage-Body(Beispiel):..............................................................................................................

###### {

"title":"Grafikdesign-Paket",
"image":null,
"description":"EinumfassendesGrafikdesign-PaketfürUnternehmen.",
"details":[
{
"title":"BasicDesign",
"revisions":2,
"delivery_time_in_days":5,
"price":100.00,
"features":["LogoDesign","Visitenkarte"],
"offer_type":"basic"
},
{
"title":"StandardDesign",
"revisions":5,
"delivery_time_in_days":7,
"price":200.00,
"features":["LogoDesign","Visitenkarte","Briefpapier"],
"offer_type":"standard"
},
{
"title":"PremiumDesign",
"revisions":10,
"delivery_time_in_days":10,
"price":500.00,
"features":["LogoDesign","Visitenkarte","Briefpapier","Flyer"],
"offer_type":"premium"
}
]
}

**Antwort(beiErfolg):**

###### {

"id":1,
"title":"Grafikdesign-Paket",
"image":null,
"description":"EinumfassendesGrafikdesign-PaketfürUnternehmen.",
"details":[
{
"id":1,
"title":"BasicDesign",
"revisions":2,
"delivery_time_in_days":5,
"price":100.00,
"features":["LogoDesign","Visitenkarte"],
"offer_type":"basic"
},
{
"id":2,
"title":"StandardDesign",
"revisions":5,
"delivery_time_in_days":7,
"price":200.00,
"features":["LogoDesign","Visitenkarte","Briefpapier"],
"offer_type":"standard"
},
{
"id":3,
"title":"PremiumDesign",
"revisions":10,
"delivery_time_in_days":10,
"price":500.00,
"features":["LogoDesign","Visitenkarte","Briefpapier","Flyer"],
"offer_type":"premium"
}
]
}

**3.GET/offers/{id}/**

##### Beschreibung:....................................................................................................................................

DieserEndpunktgibtdieDetailseinesspezifischenAngebotszurück.

##### Anfragemethoden:..........................................................................................................................

###### GET

##### URL-Parameter:.................................................................................................................................

```
id:DieIDdesgewünschtenAngebots.
```

##### BeispielfüreineAnfrage:.............................................................................................................

GET/offers/1/

**Antwort:**
{
"id":1,
"user":1,
"title":"Grafikdesign-Paket",
"image":null,
"description":"EinumfassendesGrafikdesign-PaketfürUnternehmen.",
"created_at":"2024-09-25T10:00:00Z",
"updated_at":"2024-09-28T12:00:00Z",
"details":[
{
"id":1,
"title":"BasicDesign",
"revisions":2,
"delivery_time_in_days":5,
"price":100.00,
"features":["LogoDesign","Visitenkarte"],
"offer_type":"basic"
},
{
"id":2,
"title":"StandardDesign",
"revisions":5,
"delivery_time_in_days":7,
"price":200.00,
"features":["LogoDesign","Visitenkarte","Briefpapier"],
"offer_type":"standard"
},
{
"title":"PremiumDesign",
"revisions":10,
"delivery_time_in_days":10,
"price":500.00,
"features":["LogoDesign","Visitenkarte","Briefpapier","Flyer"],
"offer_type":"premium"
}
],

"min_price":100.00,
"min_delivery_time":5,
"user_details":{
"first_name":"John",
"last_name":"Doe",
"username":"jdoe"
}
}

#### 4.PATCH/offers/{id}/................................................................................................................................

##### Beschreibung:..................................................................................................................................

##### Beschreibung:....................................................................................................................................

AktualisierteinspezifischesAngebot.EinPATCHüberschreibtnurdieangegebenen
Felder.

##### Anfragemethoden:........................................................................................................................

###### PATCH

##### URL-Parameter:..............................................................................................................................

```
id:DieIDdeszuaktualisierendenAngebots.
```

##### Anfrage-Body(BeispielfürPATCH):...................................................................................

###### {

"title":"UpdatedGrafikdesign-Paket",
"details":[
{
"title":"BasicDesignUpdated",
"revisions":3,
"delivery_time_in_days":6,
"price":120.00,
"features":["LogoDesign","Flyer"],
"offer_type":"basic"
}
]
}

**Antwort(beiErfolg):**
{
"id":1,
"title":"UpdatedGrafikdesign-Paket",
"details":[
{
"id":1,
"title":"BasicDesignUpdated",
"revisions":3,

"delivery_time_in_days":6,
"price":120.00,
"features":["LogoDesign","Flyer"],
"offer_type":"basic"
}
]
}

#### 5.DELETE/offers/{id}/................................................................................................................................

##### Beschreibung:...................................................................................................................................

##### Beschreibung:...................................................................................................................................

LöschteinspezifischesAngebot.

##### Anfragemethoden:.........................................................................................................................

##### Anfragemethoden:.........................................................................................................................

###### DELETE

##### URL-Parameter:...............................................................................................................................

##### URL-Parameter:...............................................................................................................................

```
id:DieIDdeszulöschendenAngebots.
```

##### BeispielfüreineAnfrage:............................................................................................................

##### BeispielfüreineAnfrage:............................................................................................................

DELETE/offers/1/

##### Antwort(beiErfolg)Hinweis,dasistnicht“204NoContent”:...............................

{}

#### 6.GET/offerdetails/{id}/............................................................................................................................

**Beschreibung:**

RuftdieDetailseinesspezifischenAngebotsdetailsab.

**Anfragemethoden:**

```
GET
```

**URL-Parameter:**

```
id:DieIDdesAngebotsdetails.
```

**BeispielfüreineAnfrage:**

GET/offerdetails/1/

**Antwort:**
{

"id":1,
"title":"BasicDesign",
"revisions":2,
"delivery_time_in_days":5,
"price":100.00,
"features":["LogoDesign","Visitenkarte"],
"offer_type":"basic"
}

#### 7.AllgemeinePermissions:........................................................................................

-NurUserdieAuthentifiziertundownervondemAngebotsind(oderAdmin),
könnendieslöschen oderbearbeiten.
-NurAnbieterkönnenAngeboteerstellen

### DokumentationfürdieBackend-EndpunktezuBestellungen........................................................

DieseAPI-DokumentationbeschreibtdieEndpunkte,diefürdieVerwaltungvon
Bestellungen(Orders)implementiertsind.DieEndpunktedeckensowohldas
ErstellenalsauchdasAbrufen,AktualisierenundLöschenvonBestellungenab.
ZusätzlichwirddieStrukturundFunktionalitätderSerializerundModelleerläutert,
umeinbesseresVerständnisderAPI-Interaktionenzuermöglichen.

### API-Endpunkte................................................................................................................................................

DieAPIbietetfolgendeEndpunktefürdas **Order** -Modell:

1. **GET/orders/** – ListederBestellungendesangemeldetenBenutzers.
2. **POST/orders/** – ErstelleneinerneuenBestellungbasierendaufeinem
   Angebot(Offer).
3. **GET/orders/{id}/** – AbrufenderDetailseinerspezifischenBestellung.
4. **PATCH/orders/{id}/** – AktualisierendesStatuseinerspezifischen
   Bestellung.
5. **DELETE/orders/{id}/** – LöscheneinerBestellung(nurdurchAdmins).

### EndpunkteimDetail.....................................................................................................................................

### 1.GET/orders/.................................................................................................................................................

#### Beschreibung:..................................................................................................................................

#### Beschreibung:..................................................................................................................................

DieserEndpunktgibteineListederBestellungenzurück,dieentwedervondem
BenutzeralsKundeoderalsGeschäftspartnererstelltwurden.

#### Anfragemethoden:........................................................................................................................

###### GET

#### Antwort(Beispiel):.........................................................................................................................

###### [

###### {

"id":1,
"customer_user":1,
"business_user":2,
"title":"LogoDesign",
"revisions":3,
"delivery_time_in_days":5,
"price":150.00,
"features":["LogoDesign","Visitenkarten"],
"offer_type":"basic",
"status":"in_progress",
"created_at":"2024-09-29T10:00:00Z",
"updated_at":"2024-09-30T12:00:00Z"
}
]

#### Query-Parameter:..........................................................................................................................

```
KeinespezifischenParameter.
```

#### Hinweis:...............................................................................................................................................

```
NurBestellungen,dievomangemeldetenBenutzerentwederals Kunde oder
als Geschäftspartner erstelltwurden,werdenzurückgegeben.
```

### 2.POST/orders/.............................................................................................................................................

**Beschreibung:**

ErstelleneinerneuenBestellungbasierendaufdenDetailseinesAngebots
(OfferDetail).

#### Anfragemethoden:........................................................................................................................

#### Anfragemethoden:........................................................................................................................

###### POST

#### Anfrage-Body(Beispiel):............................................................................................................

###### {

"offer_detail_id": 1
}

**Antwort(beiErfolg):**

{
"id":2,
"customer_user":1,
"business_user":3,
"title":"WebsiteDevelopment",
"revisions":5,
"delivery_time_in_days":10,
"price":500.00,
"features":["Homepage","ResponsiveDesign"],
"offer_type":"premium",
"status":"in_progress",
"created_at":"2024-09-30T12:30:00Z",
"updated_at":"2024-09-30T12:30:00Z"
}

#### Hinweis:..............................................................................................................................................

```
NurBenutzermiteinem CustomerProfile könnenBestellungenerstellen.
DerBenutzergibteine OfferDetailID an,unddieBestellungwirdaufder
GrundlagediesesAngebotserstellt.
BeachtedasdieofferdennochbeinhaltenmusswerderAnbieterundwerder
Kundeist,daskannausderAuthundderOfferentnommenwerden
```

### 3.GET/orders/{id}/......................................................................................................................................

#### Beschreibung:..................................................................................................................................

AbrufenderDetailseinerspezifischenBestellunganhandderID.

#### Anfragemethoden:........................................................................................................................

###### GET

#### URL-Parameter:..............................................................................................................................

#### URL-Parameter:..............................................................................................................................

```
id :DieIDderzuabrufendenBestellung.
```

#### BeispielfüreineAnfrage:...........................................................................................................

GET/orders/1/

**Antwort:**

{
"id":1,
"customer_user":1,
"business_user":2,
"title":"LogoDesign",
"revisions":3,
"delivery_time_in_days":5,
"price":150.00,
"features":["LogoDesign","Visitenkarten"],
"offer_type":"basic",
"status":"in_progress",
"created_at":"2024-09-29T10:00:00Z",
"updated_at":"2024-09-30T12:00:00Z"
}

### 4.PATCH/orders/{id}/...............................................................................................................................

#### Beschreibung:..................................................................................................................................

AktualisierendesStatuseinerBestellung(z.B.von"in_progress"zu"completed"oder
"cancelled").

**Anfragemethoden:**

```
PATCH
```

**URL-Parameter:**

```
id :DieIDderzuaktualisierendenBestellung.
```

#### Anfrage-Body(Beispiel):............................................................................................................

###### {

"status":"completed"
}

**Antwort(beiErfolg):**

{
"id":1,
"customer_user":1,
"business_user":2,
"title":"LogoDesign",
"revisions":3,
"delivery_time_in_days":5,
"price":150.00,
"features":["LogoDesign","Visitenkarten"],
"offer_type":"basic",
"status":"completed",
"created_at":"2024-09-29T10:00:00Z",
"updated_at":"2024-09-30T15:00:00Z"
}

#### Hinweis:..............................................................................................................................................

```
DerBenutzerkannnurdenStatusaktualisieren.
EinevollständigeAktualisierungderBestellung(PUT)istnichterlaubt.
```

### 5.DELETE/orders/{id}/..............................................................................................................................

#### Beschreibung:..................................................................................................................................

LöscheneinerspezifischenBestellung.NurAdmin-Benutzer(Staff)dürfen
Bestellungenlöschen.

#### Anfragemethoden:........................................................................................................................

###### DELETE

#### URL-Parameter:...............................................................................................................................

#### URL-Parameter:...............................................................................................................................

```
id :DieIDderzulöschendenBestellung.
```

#### BeispielfüreineAnfrage:...........................................................................................................

#### BeispielfüreineAnfrage:...........................................................................................................

DELETE/orders/1/

**Antwort(beiErfolg),beachte,dassdasnicht“204NoContent”ist:**

{}

## ErweiterteAPIfürdasZählenvonBestellungen....................................................................................

DieseDokumentationbeschreibtdiezusätzlichenEndpunktefürdasZählender
BestellungeneinesGeschäftsnutzers(BusinessUser).DieAPIermöglichtes,die
Anzahlder **abgeschlossenen** und **laufenden** Bestellungenfüreinenbestimmten
Geschäftsnutzerabzurufen.

### API-Endpunkte................................................................................................................................................

DieAPIbietetzweiEndpunkte,diespezifischfürGeschäftsnutzersind:

1. **GET/order-count/{business_user_id}/** – GibtdieAnzahlder **laufenden**
   BestellungeneinesGeschäftsnutzerszurück.
2. **GET/completed-order-count/{business_user_id}/** – GibtdieAnzahlder
   **abgeschlossenen** BestellungeneinesGeschäftsnutzerszurück.

### EndpunkteimDetail.....................................................................................................................................

### 1.GET/order-count/{business_user_id}/...........................................................................................

#### Beschreibung:..................................................................................................................................

```
DieserEndpunktgibtdieAnzahlder laufenden Bestellungeneines
bestimmtenGeschäftsnutzers(BusinessUser)zurück.Laufende
BestellungensindsolchemitdemStatusin_progress.
```

#### Anfragemethoden:........................................................................................................................

###### GET

**URL-Parameter:**

```
business_user_id :DieIDdesGeschäftsnutzers,dessenlaufendeBestellungen
gezähltwerdensollen.
```

#### BeispielfüreineAnfrage:...........................................................................................................

GET/order-count/2/

**Antwort(Beispiel):**

###### {

"order_count": 5
}

#### Fehlerfälle:.........................................................................................................................................

#### Fehlerfälle:.........................................................................................................................................

```
WennderGeschäftsnutzernichtgefundenwird:
```

###### {

"error":"Businessusernotfound."
}

#### Hinweis:..............................................................................................................................................

```
NurBestellungenmitdemStatusin_progresswerdengezählt.
```

### 2.GET/completed-order-count/{business_user_id}/.................................................

#### Beschreibung:..................................................................................................................................

```
GibtdieAnzahlder abgeschlossenen Bestellungeneinesbestimmten
Geschäftsnutzerszurück.AbgeschlosseneBestellungenhabendenStatus
completed.
```

#### Anfragemethoden:........................................................................................................................

###### GET

#### URL-Parameter:..............................................................................................................................

```
business_user_id :DieIDdesGeschäftsnutzers,dessenlaufendeBestellungen
gezähltwerdensollen.
```

**BeispielfüreineAnfrage:**

GET/completed-order-count/2/

**Antwort(Beispiel):**

###### {

```
"completed_order_count": 10
```

###### }

**Fehlerfälle:**

```
WennderGeschäftsnutzernichtgefundenwird:
```

###### {

"error":"Businessusernotfound."
}

#### Hinweis:..........................................................................................................

```
NurBestellungenmitdemStatuscompletedwerdengezählt.
```

### Zusammenfassung:......................................................................................................................................

```
BeideEndpunkteermöglichenes,dieAnzahlvonBestellungeneines
Geschäftsnutzerszuzählen,entwederlaufendeoderabgeschlossene.
DieseAbfrageunterliegtkeinenpermissions.
```

## DokumentationdesAPI-EndpunktsfürBasisinformationen...........................................................

DieserEndpunktbietetallgemeineStatistikenüberdiePlattform,wiez.B.dieAnzahlder
Bewertungen,dasdurchschnittlicheBewertungsergebnis,dieAnzahlderGeschäftsnutzer
unddieAnzahlderAngebote.

### 1.GET/base-info/......................................................................................................

#### Beschreibung:..................................................................................................................................

```
RuftallgemeineBasisinformationenzurPlattformab,einschließlichder
AnzahlderBewertungen,desdurchschnittlichenBewertungsergebnisses,der
AnzahlderGeschäftsnutzer(BusinessProfile)undderAnzahlderAngebote.
```

#### Anfragemethoden:........................................................................................................................

###### GET

#### URL-Parameter:...............................................................................................................................

```
Keine
```

#### BeispielfüreineAnfrage:...........................................................................................................

GET/base-info/

**Antwort(Beispiel):**

{
"review_count":10,
"average_rating":4.6,
"business_profile_count":45,
"offer_count":150,
}

#### Felder:............................................................................................................

```
review_count:DieGesamtzahlderBewertungenaufderPlattform.
average_rating:DasdurchschnittlicheBewertungsergebnisallerBewertungen
(Skala: 0 bis5,aufeineDezimalstellegerundet).
business_profile_count:DieAnzahlderregistriertenGeschäftsnutzer
(BusinessProfile).
offer_count:DieGesamtzahldererstelltenAngeboteaufderPlattform.
```

## API-EndpunktefürBenutzerprofile.............................................................................................................

### 1.GET/profile/<int:pk>/.............................................................................................

#### Beschreibung:.................................................................................................

```
RuftdiedetailliertenInformationeneinesBenutzerprofilsab(sowohlfür
Kunden-alsauchfürGeschäftsnutzer).ErmöglichtauchdasBearbeitender
Profildaten(PATCH).
```

#### Anfragemethoden:..........................................................................................

```
GET:LiefertdievollständigenProfildateneinesspezifischenBenutzers.
PATCH:ErmöglichteseinemBenutzeroderAdmin,bestimmte
Profilinformationenzuaktualisieren.
```

#### URL-Parameter:.............................................................................................

```
pk:DieIDdesBenutzers,dessenProfilabgerufenoderbearbeitetwird.
```

**ErfolgreicheAntwortaufGET(Beispiel):**

{
"user":1, //idbzwpkdesusers
"username":"max_mustermann",

"first_name":"Max",
"last_name":"Mustermann",
"file":"profile_picture.jpg",
"location":"Berlin",
"tel":"123456789",
"description":"Businessdescription",
"working_hours":"9-17",
"type":"business",
"email":"max@business.de",
"created_at":"2023-01-01T12:00:00"
}

**ErfolgreicheAntwortaufPATCH(Beispiel):**

{
"location":"Berlin",
"tel":"123456789",
"description":"Businessdescription",
"working_hours":"9-17",
"type":"business",
"email":"max@business.de"
}

**Statuscodes:**

```
200 OK:Erfolgreichabgerufen.
400 BadRequest:UngültigeoderfehlendeFelder.
403 Forbidden:Berechtigungsfehler.
404 NotFound:Profilnichtgefunden.
```

### 2.GET/profiles/business/..........................................................................................

#### Beschreibung:.................................................................................................

```
GibteineListeallerGeschäftsnutzeraufderPlattformzurück.
```

#### Anfragemethoden:..........................................................................................

###### GET

#### BeispielfüreineAnfrage:...............................................................................

#### BeispielfüreineAnfrage:...............................................................................

###### [

###### {

"user":{
"pk":1,
"username":"max_business",
"first_name":"Max",
"last_name":"Mustermann"
},
"file":"profile_picture.jpg",
"location":"Berlin",
"tel":"123456789",
"description":"Businessdescription",
"working_hours":"9-17",
"type":"business"
}
]

**Statuscodes:**

```
200 OK:Erfolgreichabgerufen.
```

### 3.GET/profiles/customer/..........................................................................................

#### Beschreibung:.................................................................................................

```
GibteineListeallerKundenprofileaufderPlattformzurück.
```

#### Anfragemethoden:..........................................................................................

###### GET

**BeispielfüreineAnfrage:**

[
{
"user":{
"pk":2,
"username":"customer_jane",
"first_name":"Jane",
"last_name":"Doe"
},
"file":"profile_picture_customer.jpg",
"uploaded_at":"2023-09-15T09:00:00",
"type":"customer"
}
]

**Statuscodes:**

```
200 OK:Erfolgreichabgerufen.
```

### Zusammenfassung:......................................................................................................................................

DieAPIbietetsowohleineDetailansichtalsaucheineListenansichtfür
Benutzerprofile.GeschäftsnutzerundKundenprofilekönnenjeweilseinzelnoderals
Listeabgerufenwerden,wobeisowohlGETalsauchPUT/PATCHfürdasBearbeiten
vonProfildatenunterstütztwerden.

## Authentifizierungs-undRegistrierungs-API...........................................................................................

### 1.POST/login/...........................................................................................................

#### Beschreibung:.................................................................................................

#### Beschreibung:.................................................................................................

```
AuthentifizierteinenBenutzerundlieferteinAuthentifizierungs-Token
zurück,dasfürweitereAPI-Anfragengenutztwird.
```

#### Anfragemethoden:..........................................................................................

#### Anfragemethoden:..........................................................................................

###### POST

#### ErforderlicheFelder:.......................................................................................

#### ErforderlicheFelder:.......................................................................................

```
username:BenutzernamedesNutzers.
password:PasswortdesNutzers.
```

#### Antwort:..........................................................................................................

```
ErfolgreicheAuthentifizierunggibteinTokensowieBenutzerinformationen
zurück.
```

{
"token":"abcd1234",
"username":"max_mustermann",
"email":"max@beispiel.de",
"user_id": 1
}

**Statuscodes:**

```
200 OK:ErfolgreicheAnmeldung.
400 BadRequest:FalscheAnmeldeinformationenoderungültigeEingabe.
```

### 2.POST/registration/.................................................................................................

**Beschreibung:**

```
RegistrierteinenneuenBenutzerunderstelltdasentsprechende
Benutzerprofil.NacherfolgreicherRegistrierungwirdein
Authentifizierungs-Tokenzurückgegeben.
```

**Anfragemethoden:**

```
POST
```

**ErforderlicheFelder:**

```
username:BenutzernamedesneuenNutzers.
email:E-Mail-AdressedesneuenNutzers.
password:PasswortfürdenneuenBenutzer.
repeated_password:WiederholungdesPasswortszurBestätigung.
type:Profiltyp(Geschäfts-oderKundenprofil).
```

#### Antwort:..........................................................................................................

```
ErfolgreicheRegistrierunggibteinTokensowiedieBenutzerinformationen
zurück.
```

**Antwort(Beispiel):**
{
"token":"abcd1234",
"username":"jane_doe",
"email":"jane@beispiel.de",
"user_id": 2
}

#### Statuscodes:...................................................................................................

```
200 OK:ErfolgreicheRegistrierung.
400 BadRequest:UngültigeEingabenoderwennz.B.dieE-Mailbereits
existiert.
```

### Zusammenfassung:.....................................................................................................................................

DieseAPIbietetEndpunktefürdieBenutzeranmeldungund-registrierung.Durch
denLoginerhältderBenutzereinTokenfürdieAuthentifizierung,undbeider
RegistrierungwirdeinneuerBenutzererstellt,wobeieinKunden-oder
Geschäftsnutzerprofilautomatischzugewiesenwird.

Umsicherzustellen,dassdieFehlervonderAPIkonsistentundbenutzerfreundlich
dargestelltwerden,solltetihrdaraufachten,dassdiezurückgegebenenFehlereine
klareStrukturhaben,dieeureFunktionextractErrorMessageskorrektverarbeiten
kann.HiersindeinpaarTipps,wiedieAPI-Fehleraussehensollten:

## APIFehlerstruktur:...........................................................................................................

### 1.AllgemeinerFehleraufbau:.....................................................................................

FehlersolltenalsJSON-Objektezurückgegebenwerden.DasObjektsollte
Schlüssel-Werte-Paareenthalten,beidenenderSchlüsseldasfehlerhafteFeldoder
dieFehlermeldungistundderWertentwedereineListevonFehlernodereine
einzelneFehlermeldung.

**BeispielfüreinefehlgeschlageneValidierung:**

{
"username":["DieserBenutzernameistbereitsvergeben."],
"email":["DieseE-Mail-Adressewirdbereitsverwendet."],
}

### 2.WennmehrereFelderFehlerhaben:.....................................................................

JederFehlersollteineinerListevonNachrichten(Strings)sein,selbstwennnurein
FehlerproFeldvorhandenist.SokannextractErrorMessageskorrektarbeiten.

**BeispielfürmehrereFeldfehler:**

{
"email":["E-Mailisterforderlich.","E-Mail-Formatistungültig."],
"password":["DasPasswortistnichtgleichmitdemwiederholtenPasswort"]
}

### 3.AllgemeinerFehlerohnespezifischeFelder(z.B.Authentifizierungsfehler):.........

FallseinallgemeinerFehlerauftritt,sollteeineFehlermeldungalsListeuntereinem
allgemeinenSchlüsselwiedetailodernon_field_errorszurückgegebenwerden.

**Beispiel:**

{
"detail":["FalscheAnmeldedaten."]
}

Beachte,dasnichtfürjedeAnfrageeintoasterrorhinterlegtist.

**Endpoint:Review-Listenansichtund-Erstellung**

**URL:** /reviews/

**Beschreibung:**
ListetalleverfügbarenBewertungenaufodererstellteineneueBewertungfüreinen
Geschäftsbenutzer,fallsderBenutzerauthentifiziertistundeineKundenrollehat.

**Anfragemethoden:**

```
● GET:RufteineListeallerBewertungenab,dienachupdated_atoder
ratinggeordnetwerdenkönnen.
● POST:ErstellteineneueBewertung.NurauthentifizierteBenutzer,dieein
Kundenprofilbesitzen,könnenBewertungenerstellen.EinBenutzerkannpro
GeschäftsprofilnureineBewertungabgeben.
```

**URL-Parameter:**

```
● Keine(verwendenSieFilter-ParameterfürgezielteAbfragen)
```

**Filter-Parameter:**

```
● business_user_id:IDdesGeschäftsbenutzers,fürdenBewertungen
gefiltertwerdensollen.
● reviewer_id:IDdesBenutzers,derdieBewertungerstellthat.
```

**BeispielfüreineAnfrage:**

```
● GET /reviews/?business_user_id=1&ordering=rating
```

**Antwort(GET):**

###### [

###### {

```
"id": 1,
"business_user": 2,
"reviewer": 3,
"rating": 4,
"description": "Sehr professioneller Service.",
"created_at": "2023-10-30T10:00:00Z",
"updated_at": "2023-10-31T10:00:00Z"
},
{
"id": 2,
"business_user": 5,
"reviewer": 3,
"rating": 5,
"description": "Top Qualität und schnelle Lieferung!",
"created_at": "2023-09-20T10:00:00Z",
"updated_at": "2023-09-20T12:00:00Z"
}
```

]

**Antwort(POST):**

###### {

```
"id": 3,
"business_user": 2,
"reviewer": 3,
"rating": 5,
"description": "Hervorragende Erfahrung!",
"created_at": "2023-10-30T15:30:00Z",
"updated_at": "2023-10-30T15:30:00Z"
```

}

**AllgemeinePermissions:**

```
● POST-Berechtigungen:NurauthentifizierteBenutzermiteinemKundenprofil
dürfenBewertungenerstellen.
● JederauthentifizierteBenutzerkannBewertungenlesen.
```

**Endpoint:Einzelansicht,AktualisierungundLöschungeinerBewertung**

**URL:** /reviews/{id}/

**Beschreibung:**
RuftdieDetailseinerspezifischenBewertungab,aktualisiertsieteilweiseoder
löschtsie.NurderErstellerderBewertungodereinAdminkanneineBewertung
löschenoderbearbeiten.

**Anfragemethoden:**

```
● GET:RuftdieDetailseinereinzelnenBewertungab.
● PATCH:AktualisiertausgewählteFelderderBewertung(nurratingund
descriptionsindeditierbar).
● DELETE:LöschtdieBewertung.NurderErstellerodereinAdminkanndie
Bewertunglöschen.
```

**URL-Parameter:**

```
● id:DieIDderspezifischenBewertung.
```

**BeispielfüreineAnfrage:**

```
● GET /reviews/1/
```

**Antwort(GET):**

###### {

```
"id": 1,
"business_user": 2,
"reviewer": 3,
"rating": 4,
"description": "Sehr professioneller Service.",
"created_at": "2023-10-30T10:00:00Z",
"updated_at": "2023-10-31T10:00:00Z"
```

}

**Antwort(PATCH):**

###### {

```
"id": 1,
"business_user": 2,
"reviewer": 3,
"rating": 5,
"description": "Noch besser als erwartet!",
```

```
"created_at": "2023-10-30T10:00:00Z",
"updated_at": "2023-11-01T08:00:00Z"
```

}

**Antwort(DELETE):**

Status 204 No Content

**AllgemeinePermissions:**

```
● PATCH,DELETE:NurderErstellerderBewertungodereinAdmindarfdiese
Aktionenausführen.
● GET:KeinebesonderenBerechtigungen,alleBenutzerkönnenBewertungen
einsehen.
```
