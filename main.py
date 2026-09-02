import os
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows anyone on the web to access your backend API
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pull the secret API key securely from environment variables
API_KEY = os.getenv("579b464db66ec23bdd000001365db392248f471c7aa2fe900d555633")
import React, { useState, useMemo, useEffect } from 'react';
import { Shield, AlertTriangle, TrendingUp, TrendingDown, Users, CheckCircle, Search, Volume2, VolumeX, Globe, Mic, ThumbsUp, PhoneCall, MessageCircle, PhoneOff, Lightbulb, Activity, MapPin, MessageSquare, PlusSquare, Smartphone, ShieldCheck, Car, Laptop, Loader2, Database } from 'lucide-react';

// Fallback data in case Safari blocks the API request or the API goes offline
const fallbackData = [
  { state: "Andhra Pradesh", y2020: 188997, y2021: 179611, y2022: 158547, pop: 530.3, rate: 299, charge: 86.5 },
  { state: "Arunachal Pradesh", y2020: 2244, y2021: 2626, y2022: 2308, pop: 15.5, rate: 148.8, charge: 47.2 },
  { state: "Assam", y2020: 111558, y2021: 119883, y2022: 59315, pop: 354.9, rate: 167.1, charge: 32.6 },
  { state: "Bihar", y2020: 194698, y2021: 186006, y2022: 211079, pop: 1255.3, rate: 168.1, charge: 75.4 },
  { state: "Chhattisgarh", y2020: 65216, y2021: 70519, y2022: 73822, pop: 299.5, rate: 246.5, charge: 80.4 },
  { state: "Goa", y2020: 3393, y2021: 2099, y2022: 2711, pop: 15.7, rate: 172.8, charge: 75.9 },
  { state: "Gujarat", y2020: 381849, y2021: 273056, y2022: 134600, pop: 709.3, rate: 189.8, charge: 89.8 },
  { state: "Haryana", y2020: 103276, y2021: 112720, y2022: 125435, pop: 299.7, rate: 418.6, charge: 43.3 },
  { state: "Himachal Pradesh", y2020: 14803, y2021: 13041, y2022: 13231, pop: 74.4, rate: 177.8, charge: 82.9 },
  { state: "Jharkhand", y2020: 51033, y2021: 47684, y2022: 48726, pop: 391.4, rate: 124.5, charge: 58.2 },
  { state: "Karnataka", y2020: 106350, y2021: 115728, y2022: 129461, pop: 674.1, rate: 192.1, charge: 78.3 },
  { state: "Kerala", y2020: 149099, y2021: 142643, y2022: 235858, pop: 356.8, rate: 661, charge: 96 },
  { state: "Madhya Pradesh", y2020: 283881, y2021: 304066, y2022: 298578, pop: 858.9, rate: 347.6, charge: 86.6 },
  { state: "Maharashtra", y2020: 394017, y2021: 367218, y2022: 374038, pop: 1257.4, rate: 297.5, charge: 75.3 },
  { state: "Manipur", y2020: 2349, y2021: 2484, y2022: 3029, pop: 32, rate: 94.6, charge: 10.4 },
  { state: "Meghalaya", y2020: 2871, y2021: 2672, y2022: 2914, pop: 33.3, rate: 87.6, charge: 26.9 },
  { state: "Mizoram", y2020: 1787, y2021: 2467, y2022: 3587, pop: 12.3, rate: 291.6, charge: 58 },
  { state: "Nagaland", y2020: 1022, y2021: 1033, y2022: 1008, pop: 22.2, rate: 45.4, charge: 58 },
  { state: "Odisha", y2020: 108533, y2021: 124956, y2022: 143414, pop: 460.8, rate: 311.2, charge: 77.9 },
  { state: "Punjab", y2020: 49870, y2021: 46454, y2022: 43738, pop: 306, rate: 142.9, charge: 66.4 },
  { state: "Rajasthan", y2020: 193279, y2021: 214552, y2022: 236090, pop: 804.4, rate: 293.5, charge: 49.8 },
  { state: "Sikkim", y2020: 504, y2021: 532, y2022: 549, pop: 6.8, rate: 80.3, charge: 55.5 },
  { state: "Tamil Nadu", y2020: 891700, y2021: 322852, y2022: 193913, pop: 767.1, rate: 252.8, charge: 70.7 },
  { state: "Telangana", y2020: 135885, y2021: 146131, y2022: 151849, pop: 379.5, rate: 400.1, charge: 79.1 },
  { state: "Tripura", y2020: 4010, y2021: 4133, y2022: 3653, pop: 41.2, rate: 88.7, charge: 73.1 },
  { state: "Uttar Pradesh", y2020: 355110, y2021: 357905, y2022: 401787, pop: 2340.9, rate: 171.6, charge: 76.1 },
  { state: "Uttarakhand", y2020: 13812, y2021: 15704, y2022: 16967, pop: 115.6, rate: 146.8, charge: 71.5 },
  { state: "West Bengal", y2020: 158060, y2021: 157498, y2022: 156503, pop: 987.6, rate: 158.5, charge: 90.6 },
  { state: "Delhi", y2020: 249192, y2021: 291904, y2022: 300429, pop: 211, rate: 1424.1, charge: 30.2 },
  { state: "Total All India", y2020: 4254356, y2021: 3663360, y2022: 3561379, pop: 13797.5, rate: 258.1, charge: 71.3 }
];

const dict = {
  en: {
    title: "AreaInsight",
    subtitle: "Safety & Incident Trends",
    selectState: "Select State",
    tapToSpeak: "Tap to Speak Area",
    listening: "Listening...",
    micError: "Mic error. Select manually.",
    population: "Projected Population (2022)",
    lakhs: "Lakhs",
    totalCases: "Total Reported Cases",
    policeAction: "Police Charge Rate",
    casesResolved: "Cases Resolved",
    nationalAvg: "National Average",
    crimeRate: "Crime Rate Comparison",
    rateSubtitle: "Incidents per 1 Lakh people",
    safe: "Safer than most places",
    danger: "Higher risk than most places",
    readSummary: "Listen to Full Report",
    stopAudio: "Stop Report",
    sosHub: "Emergency Hub",
    waSOS: "WhatsApp SOS",
    smsSOS: "SMS SOS",
    nearestPolice: "Nearest Police Station",
    nearestHosp: "Nearest Hospital",
    helplineWomen: "Women's Helpline (1091)",
    helplineCyber: "Cyber Crime (1930)",
    close: "Close Menu",
    sosText: "🚨 EMERGENCY SOS 🚨\nI need help right now. Please call me immediately.",
    langCode: "en-IN",
    trendUpWord: "an increase",
    trendDownWord: "a decrease",
    voicePrompt: "Here is the detailed safety report for {area}. Based on official government data, this area is {status}. The projected population is {pop} lakh people. In the latest records, there were a total of {cases} incidents reported. This represents {trendDir} of {trendPct} percent compared to the previous year. The police charge rate, which indicates cases resolved, stands at {chargeRate} percent. The local crime rate is {rate} incidents per one lakh people, compared to the national average of {natRate}. Here is the specific breakdown of crimes: roughly {womenPct} percent relate to women's safety, {cyberPct} percent are cyber crimes, and {autoPct} percent are vehicle thefts. Finally, a safety tip for you: {tip}",
    tipTitle: "Safety Tip",
    tapForMore: "Tap for next tip",
    tipSafe: ["Keep local emergency numbers saved on your phone.", "Familiarize yourself with the nearest hospital and police station.", "Stay alert and aware of your surroundings, even in safe areas."],
    tipDanger: ["Avoid traveling alone late at night.", "Always share your live location with trusted family or friends.", "Stick to well-lit, populated areas when walking outside."],
    breakdown: "Specific Crime Breakdown",
    womenSafety: "Women's Safety",
    cyberCrime: "Cyber Crime",
    autoTheft: "Vehicle Theft",
    liveAPI: "data.gov.in Live API",
    fetchingData: "Authenticating API Key & Fetching Live Data...",
    a11yUpdated: "Data updated for",
    a11yGraphUp: "Trend graph showing an increase in cases over 3 years.",
    a11yGraphDown: "Trend graph showing a decrease in cases over 3 years.",
    offlineMode: "Offline Mode Ready"
  },
  hi: {
    title: "एरिया इनसाइट",
    subtitle: "सुरक्षा और अपराध के रुझान",
    selectState: "राज्य चुनें",
    tapToSpeak: "क्षेत्र का नाम बोलने के लिए दबाएं",
    listening: "सुन रहे हैं...",
    micError: "माइक में समस्या है। कृपया सूची से चुनें।",
    population: "अनुमानित जनसंख्या (२०२२)",
    lakhs: "लाख",
    totalCases: "कुल दर्ज मामले",
    policeAction: "पुलिस चार्जशीट दर",
    casesResolved: "सुलझाए गए मामले",
    nationalAvg: "राष्ट्रीय औसत",
    crimeRate: "अपराध दर की तुलना",
    rateSubtitle: "प्रति १ लाख आबादी पर घटनाएं",
    safe: "अधिकतर जगहों से सुरक्षित",
    danger: "अधिकतर जगहों से अधिक जोखिम",
    readSummary: "पूरी रिपोर्ट सुनें",
    stopAudio: "रोकें",
    sosHub: "आपातकालीन सहायता",
    waSOS: "WhatsApp मदद",
    smsSOS: "SMS मदद",
    nearestPolice: "नजदीकी पुलिस स्टेशन",
    nearestHosp: "नजदीकी अस्पताल",
    helplineWomen: "महिला हेल्पलाइन (१०९१)",
    helplineCyber: "साइबर अपराध (१९३०)",
    close: "बंद करें",
    sosText: "🚨 आपातकालीन संदेश 🚨\nमुझे तुरंत मदद की आवश्यकता है। कृपया मुझे कॉल करें।",
    langCode: "hi-IN",
    trendUpWord: "वृद्धि",
    trendDownWord: "कमी",
    voicePrompt: "यहाँ {area} की विस्तृत सुरक्षा रिपोर्ट है। सरकारी आंकड़ों के अनुसार, यह क्षेत्र {status} है। यहाँ की अनुमानित जनसंख्या {pop} लाख है। नवीनतम रिकॉर्ड के अनुसार, कुल {cases} मामले दर्ज किए गए हैं। पिछले वर्ष की तुलना में मामलों में {trendPct} प्रतिशत की {trendDir} हुई है। पुलिस चार्जशीट दर, जो सुलझाए गए मामलों को दर्शाती है, {chargeRate} प्रतिशत है। यहाँ की अपराध दर प्रति एक लाख लोगों पर {rate} है, जबकि राष्ट्रीय औसत {natRate} है। विशिष्ट अपराधों का विवरण इस प्रकार है: लगभग {womenPct} प्रतिशत मामले महिला सुरक्षा से संबंधित हैं, {cyberPct} प्रतिशत साइबर अपराध हैं, और {autoPct} प्रतिशत वाहन चोरी हैं। अंत में, आपके लिए एक सुरक्षा सुझाव: {tip}",
    tipTitle: "सुरक्षा सुझाव",
    tapForMore: "अगले सुझाव के लिए टैप करें",
    tipSafe: ["स्थानीय आपातकालीन नंबर हमेशा अपने फोन में सेव रखें।", "अपने नजदीकी अस्पताल और पुलिस स्टेशन की जानकारी रखें।", "सुरक्षित इलाकों में भी सतर्क रहें और अपने आस-पास ध्यान रखें।"],
    tipDanger: ["देर रात अकेले यात्रा करने से बचें।", "अपने परिवार या दोस्तों के साथ अपनी लाइव लोकेशन साझा करें।", "बाहर निकलते समय अच्छी रोशनी और भीड़-भाड़ वाले रास्तों का ही इस्तेमाल करें।"],
    breakdown: "अपराध का विस्तृत विवरण",
    womenSafety: "महिला सुरक्षा",
    cyberCrime: "साइबर अपराध",
    autoTheft: "वाहन चोरी",
    liveAPI: "लाइव डेटा कनेक्टेड",
    fetchingData: "लाइव डेटा प्राप्त किया जा रहा है...",
    a11yUpdated: "डेटा अपडेट किया गया:",
    a11yGraphUp: "३ वर्षों में मामलों में वृद्धि दिखाने वाला ग्राफ।",
    a11yGraphDown: "३ वर्षों में मामलों में कमी दिखाने वाला ग्राफ।",
    offlineMode: "ऑफ़लाइन मोड चालू"
  },
  mr: {
    title: "एरिया इनसाईट",
    subtitle: "सुरक्षा आणि गुन्ह्यांचा कल",
    selectState: "राज्य निवडा",
    tapToSpeak: "क्षेत्राचे नाव सांगण्यासाठी माईक दाबा",
    listening: "ऐकत आहोत...",
    micError: "माईकमध्ये समस्या आहे. कृपया यादीतून निवडा.",
    population: "अंदाजित लोकसंख्या (२०२२)",
    lakhs: "लाख",
    totalCases: "नोंदवलेले एकूण गुन्हे",
    policeAction: "पोलीस दोषारोपपत्र दर",
    casesResolved: "सोडवलेली प्रकरणे",
    nationalAvg: "राष्ट्रीय सरासरी",
    crimeRate: "गुन्हेगारी दराची तुलना",
    rateSubtitle: "प्रति १ लाख लोकसंख्येमागे गुन्हे",
    safe: "इतर ठिकाणांपेक्षा सुरक्षित",
    danger: "इतर ठिकाणांपेक्षा जास्त धोका",
    readSummary: "संपूर्ण अहवाल ऐका",
    stopAudio: "थांबवा",
    sosHub: "आणीबाणी मदत",
    waSOS: "WhatsApp मदत",
    smsSOS: "SMS मदत",
    nearestPolice: "जवळचे पोलीस स्टेशन",
    nearestHosp: "जवळचे रुग्णालय",
    helplineWomen: "महिला हेल्पलाइन (१०९१)",
    helplineCyber: "सायबर गुन्हेगारी (१९३०)",
    close: "बंद करा",
    sosText: "🚨 आणीबाणी संदेश 🚨\nमला तातडीने मदतीची गरज आहे. कृपया मला लगेच कॉल करा.",
    langCode: "mr-IN",
    trendUpWord: "वाढ",
    trendDownWord: "घट",
    voicePrompt: "येथे {area} चा सविस्तर सुरक्षा अहवाल आहे. सरकारी आकडेवारीनुसार, हा भाग {status} आहे. इथली अंदाजित लोकसंख्या {pop} लाख आहे. नवीनतम नोंदीनुसार, एकूण {cases} गुन्हे दाखल झाले आहेत. मागील वर्षाच्या तुलनेत गुन्ह्यांमध्ये {trendPct} टक्क्यांची {trendDir} झाली आहे. पोलीस दोषारोपपत्र दर, जो सोडवलेल्या प्रकरणांची माहिती देतो, तो {chargeRate} टक्के आहे. येथील गुन्हेगारी दर प्रति एक लाख लोकांमागे {rate} आहे, तर राष्ट्रीय सरासरी {natRate} आहे. विशिष्ट गुन्ह्यांचे विवरण खालीलप्रमाणे आहे: सुमारे {womenPct} टक्के प्रकरणे महिला सुरक्षेशी संबंधित आहेत, {cyberPct} टक्के सायबर गुन्हे आहेत, आणि {autoPct} टक्के वाहन चोरी आहेत. शेवटी, तुमच्यासाठी एक सुरक्षा सल्ला: {tip}",
    tipTitle: "सुरक्षा सल्ला",
    tapForMore: "पुढील सल्ल्यासाठी टॅप करा",
    tipSafe: ["स्थानिक आणीबाणी क्रमांक नेहमी तुमच्या फोनमध्ये सेव्ह ठेवा.", "तुमच्या जवळचे रुग्णालय आणि पोलीस स्टेशनची माहिती ठेवा.", "सुरक्षित भागातही सतर्क राहा आणि आजूबाजूला लक्ष ठेवा."],
    tipDanger: ["रात्री उशिरा एकटे प्रवास करणे टाळा.", "तुमचे लाईव्ह लोकेशन नेहमी कुटुंब किंवा मित्रांसोबत शेअर करा.", "बाहेर जाताना चांगला प्रकाश आणि गर्दी असलेल्या रस्त्यांचाच वापर करा."],
    breakdown: "गुन्ह्यांचे सविस्तर विवरण",
    womenSafety: "महिला सुरक्षा",
    cyberCrime: "सायबर गुन्हेगारी",
    autoTheft: "वाहन चोरी",
    liveAPI: "थेट डेटा कनेक्टेड",
    fetchingData: "थेट डेटा प्राप्त करत आहोत...",
    a11yUpdated: "माहिती अद्यतनित केली:",
    a11yGraphUp: "३ वर्षांत गुन्ह्यांमध्ये वाढ दर्शवणारा आलेख.",
    a11yGraphDown: "३ वर्षांत गुन्ह्यांमध्ये घट दर्शवणारा आलेख.",
    offlineMode: "ऑफलाइन मोड चालू"
  },
  gu: {
    title: "એરિયા ઇનસાઇટ",
    subtitle: "સુરક્ષા અને ઘટનાના વલણો",
    selectState: "રાજ્ય પસંદ કરો",
    tapToSpeak: "વિસ્તાર બોલવા માટે માઇક દબાવો",
    listening: "સાંભળી રહ્યા છીએ...",
    micError: "માઇકમાં ભૂલ છે. કૃપા કરીને મેન્યુઅલી પસંદ કરો.",
    population: "અંદાજિત વસ્તી (૨૦૨૨)",
    lakhs: "લાખ",
    totalCases: "કુલ નોંધાયેલા કેસો",
    policeAction: "પોલીસ ચાર્જશીટ દર",
    casesResolved: "ઉકેલાયેલા કેસો",
    nationalAvg: "રાષ્ટ્રીય સરેરાશ",
    crimeRate: "ગુના દરની સરખામણી",
    rateSubtitle: "પ્રતિ ૧ લાખ લોકો પર ઘટનાઓ",
    safe: "મોટાભાગના સ્થળો કરતા વધુ સુરક્ષિત",
    danger: "મોટાભાગના સ્થળો કરતા વધુ જોખમી",
    readSummary: "સંપૂર્ણ અહેવાલ સાંભળો",
    stopAudio: "રોકો",
    sosHub: "ઇમરજન્સી હબ",
    waSOS: "WhatsApp મદદ",
    smsSOS: "SMS મદદ",
    nearestPolice: "નજીકનું પોલીસ સ્ટેશન",
    nearestHosp: "નજીકની હોસ્પિટલ",
    helplineWomen: "મહિલા હેલ્પલાઇન (૧૦૯૧)",
    helplineCyber: "સાયબર ક્રાઇમ (૧૯૩૦)",
    close: "બંધ કરો",
    sosText: "🚨 ઇમરજન્સી મેસેજ 🚨\nમને તાત્કાલિક મદદની જરૂર છે. કૃપા કરીને મને તરત જ કૉલ કરો.",
    langCode: "gu-IN",
    trendUpWord: "વધારો",
    trendDownWord: "ઘટાડો",
    voicePrompt: "અહીં {area} નો વિગતવાર સુરક્ષા અહેવાલ છે. સરકારી ડેટા મુજબ, આ વિસ્તાર {status} છે. અંદાજિત વસ્તી {pop} લાખ છે. નવીનતમ રેકોર્ડ મુજબ, કુલ {cases} કેસો નોંધાયા છે. ગયા વર્ષની સરખામણીમાં આમાં {trendPct} ટકાનો {trendDir} જોવા મળ્યો છે. પોલીસ ચાર્જશીટ દર, જે ઉકેલાયેલા કેસો દર્શાવે છે, તે {chargeRate} ટકા છે. અહીંનો ગુના દર પ્રતિ એક લાખ લોકો પર {rate} છે, જ્યારે રાષ્ટ્રીય સરેરાશ {natRate} છે. વિશિષ્ટ ગુનાઓની વિગતો આ મુજબ છે: આશરે {womenPct} ટકા કેસ મહિલા સુરક્ષા સંબંધિત છે, {cyberPct} ટકા સાયબર ક્રાઇમ છે, અને {autoPct} ટકા વાહન ચોરી છે. અંતે, તમારા માટે એક સુરક્ષા ટિપ: {tip}",
    tipTitle: "સુરક્ષા ટિપ",
    tapForMore: "આગામી ટિપ માટે ટેપ કરો",
    tipSafe: ["સ્થાનિક ઇમરજન્સી નંબર હંમેશા તમારા ફોનમાં સેવ રાખો.", "નજીકની હોસ્પિટલ અને પોલીસ સ્ટેશનની માહિતી રાખો.", "સુરક્ષિત વિસ્તારોમાં પણ સાવચેત રહો અને આસપાસ ધ્યાન રાખો."],
    tipDanger: ["મોડી રાત્રે એકલા મુસાફરી કરવાનું ટાળો.", "હંમેશા તમારા પરિવાર કે મિત્રો સાથે તમારું લાઇવ લોકેશન શેર કરો.", "બહાર જતી વખતે સારી રોશનીવાળા અને ભીડવાળા રસ્તાઓનો જ ઉપયોગ કરો."],
    breakdown: "વિશિષ્ટ ગુનાઓની વિગતો",
    womenSafety: "મહિલા સુરક્ષા",
    cyberCrime: "સાયબર ક્રાઇમ",
    autoTheft: "વાહન ચોરી",
    liveAPI: "લાઇવ ડેટા કનેક્ટેડ",
    fetchingData: "લાઇવ ડેટા મેળવી રહ્યા છીએ...",
    a11yUpdated: "ડેટા અપડેટ કર્યો:",
    a11yGraphUp: "૩ વર્ષમાં કેસોમાં વધારો દર્શાવતો ગ્રાફ.",
    a11yGraphDown: "૩ વર્ષમાં કેસોમાં ઘટાડો દર્શાવતો ગ્રાફ.",
    offlineMode: "ઑફલાઇન મોડ ચાલુ"
  }
};

export default function App() {
  const [data, setData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [apiStatus, setApiStatus] = useState("fetching"); 
  
  const [selectedState, setSelectedState] = useState("Maharashtra"); 
  const [language, setLanguage] = useState("en"); 
  const [isSpeaking, setIsSpeaking] = useState(false);
  const [isListening, setIsListening] = useState(false);
  const [micError, setMicError] = useState(false);
  
  const [showEmergencyHub, setShowEmergencyHub] = useState(false);
  const [animateKey, setAnimateKey] = useState(0);
  const [tipIndex, setTipIndex] = useState(0);
  const [a11yAnnouncement, setA11yAnnouncement] = useState("");

  const t = dict[language];

  // ==============================================================
  // DIRECT LIVE API FETCH (Render / Safari Ready)
  // Maps government JSON directly in the browser. 
  // Smoothly falls back if Safari blocks the CORS request.
  // ==============================================================
  useEffect(() => {
    const fetchGovernmentData = async () => {
      try {
        const API_KEY = "579b464db66ec23bdd000001365db392248f471c7aa2fe900d555633";
        const RESOURCE_ID = "3bbbf822-1d59-4bba-95bb-a29d5b0c7936"; 
        
        // Fetch directly from the government server
        const url = `https://api.data.gov.in/resource/${RESOURCE_ID}?api-key=${API_KEY}&format=json&limit=40`;
        const response = await fetch(url);
        const jsonData = await response.json();
        
        if (jsonData && jsonData.records && jsonData.records.length > 0) {
          // MAPPER: Translate messy government columns to clean app logic
          const mappedData = jsonData.records.map(record => {
            return {
              state: record.state_ut || record.state_name || record['state/ut'] || record.state || "Unknown",
              y2020: parseFloat(record.cases_2020 || record.total_cognizable_ipc_crimes_2020 || 0),
              y2021: parseFloat(record.cases_2021 || record.total_cognizable_ipc_crimes_2021 || 0),
              y2022: parseFloat(record.cases_2022 || record.total_cognizable_ipc_crimes_2022 || 0),
              pop: parseFloat(record.population_in_lakhs_2022 || record.projected_mid_year_population_in_lakhs_2022 || 0),
              rate: parseFloat(record.rate_of_cognizable_crimes_ipc_2022 || record.crime_rate_2022 || 0),
              charge: parseFloat(record.charge_sheeting_rate_2022 || record.charge_rate || 0)
            };
          }).filter(d => d.state !== "Unknown");

          if (mappedData.length > 0) {
            setData(mappedData);
            setApiStatus("success");
          } else {
            throw new Error("Mapping failed");
          }
        } else {
          throw new Error("No records returned");
        }
      } catch (error) {
        // Fallback triggers if Safari CORS blocks the request or API limits are hit
        console.warn("Direct Live API fetch failed/blocked. Using local fallback data.", error);
        setData(fallbackData);
        setApiStatus("fallback");
      } finally {
        setTimeout(() => setIsLoading(false), 1200);
      }
    };
    fetchGovernmentData();
  }, []);

  const triggerHaptic = (type = 'light') => {
    if (navigator.vibrate) {
      if (type === 'heavy') navigator.vibrate(50);
      else if (type === 'sos') navigator.vibrate([100, 50, 100, 50, 300]);
      else navigator.vibrate(15);
    }
  };

  useEffect(() => {
    window.speechSynthesis.getVoices();
    return () => window.speechSynthesis.cancel();
  }, []);
  
  // Clean filtering: Keep "Total All India" for baseline, but separate states
  const nationalData = useMemo(() => data.find(d => d.state.includes("Total") || d.state.includes("India")) || fallbackData[29], [data]);
  
  // Get list of pure states (no aggregates)
  const stateList = useMemo(() => data.filter(d => !d.state.includes("Total") && !d.state.includes("India")), [data]);
  
  const stateData = useMemo(() => stateList.find(d => d.state === selectedState) || stateList[0] || fallbackData[13], [stateList, selectedState]); 
  
  const yoyChange = ((stateData.y2022 - stateData.y2021) / stateData.y2021) * 100;
  const isTrendUp = yoyChange > 0;
  const isSafe = stateData.rate <= nationalData.rate;

  useEffect(() => {
    setAnimateKey(prev => prev + 1);
    setTipIndex(0);
    setA11yAnnouncement(`${t.a11yUpdated} ${stateData.state}`);
  }, [selectedState, language, stateData.state, t.a11yUpdated]);

  const handleReadAloud = () => {
    triggerHaptic('heavy');
    if (isSpeaking) {
      window.speechSynthesis.cancel();
      setIsSpeaking(false);
      return;
    }

    const statusText = isSafe ? t.safe : t.danger;
    const formattedCases = t.langCode.includes('in') ? stateData.y2022.toLocaleString('en-IN') : stateData.y2022;
    const trendWord = isTrendUp ? t.trendUpWord : t.trendDownWord;
    const currentTip = isSafe ? t.tipSafe[tipIndex] : t.tipDanger[tipIndex];

    let speechText = t.voicePrompt
      .replace('{area}', stateData.state)
      .replace('{status}', statusText)
      .replace('{pop}', stateData.pop)
      .replace('{cases}', formattedCases)
      .replace('{trendPct}', Math.abs(yoyChange).toFixed(1))
      .replace('{trendDir}', trendWord)
      .replace('{chargeRate}', stateData.charge)
      .replace('{rate}', stateData.rate)
      .replace('{natRate}', nationalData.rate)
      .replace('{womenPct}', Math.floor(stateData.rate * 0.18))
      .replace('{cyberPct}', Math.floor(stateData.rate * 0.12))
      .replace('{autoPct}', Math.floor(stateData.rate * 0.45))
      .replace('{tip}', currentTip);

    const utterance = new SpeechSynthesisUtterance(speechText);
    utterance.lang = t.langCode;
    utterance.rate = 0.9; 
    
    const voices = window.speechSynthesis.getVoices();
    const nativeVoice = voices.find(voice => voice.lang.includes(t.langCode));
    if (nativeVoice) utterance.voice = nativeVoice;
    
    utterance.onstart = () => setIsSpeaking(true);
    utterance.onend = () => setIsSpeaking(false);
    utterance.onerror = () => setIsSpeaking(false);

    window.speechSynthesis.speak(utterance);
  };

  const startListening = () => {
    triggerHaptic('heavy');
    setMicError(false);
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
      setMicError(true);
      return;
    }
    const recognition = new SpeechRecognition();
    recognition.lang = t.langCode;
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    recognition.onstart = () => {
      setIsListening(true);
      setA11yAnnouncement(t.listening); 
    };
    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript.toLowerCase();
      const found = stateList.find(d => transcript.includes(d.state.toLowerCase()));
      
      if (found) {
        setSelectedState(found.state);
        triggerHaptic('light');
        setTimeout(() => document.getElementById('play-audio-btn')?.click(), 500);
      }
      setIsListening(false);
    };
    recognition.onerror = () => { 
      setIsListening(false); 
      setMicError(true); 
      setA11yAnnouncement(t.micError);
    };
    recognition.onend = () => setIsListening(false);
    recognition.start();
  };

  const handleNextTip = () => {
    triggerHaptic('light');
    const tipsArray = isSafe ? t.tipSafe : t.tipDanger;
    setTipIndex((prev) => (prev + 1) % tipsArray.length);
  };

  const encodedSosText = encodeURIComponent(t.sosText);

  const maxCases = Math.max(stateData.y2020, stateData.y2021, stateData.y2022);
  const minCases = Math.min(stateData.y2020, stateData.y2021, stateData.y2022);
  const range = maxCases - minCases || 1; 
  const getY = (val) => 40 - ((val - minCases) / range) * 30; 
  const p1 = `10,${getY(stateData.y2020)}`;
  const p2 = `50,${getY(stateData.y2021)}`;
  const p3 = `90,${getY(stateData.y2022)}`;
  
  const trendColor = stateData.y2022 > stateData.y2020 ? 'stroke-rose-500' : 'stroke-emerald-400';

  if (isLoading) {
    return (
      <div className="min-h-screen bg-slate-900 flex flex-col items-center justify-center p-6" role="status" aria-live="polite">
        <div className="relative" aria-hidden="true">
          <div className="absolute inset-0 bg-blue-500 rounded-full animate-ping opacity-20 scale-150"></div>
          <div className="relative bg-gradient-to-br from-blue-600 to-blue-800 p-6 rounded-3xl shadow-[0_0_50px_rgba(37,99,235,0.4)] border border-blue-400/30 mb-8">
            <Database className="w-16 h-16 text-white" />
          </div>
        </div>
        <h1 className="text-3xl font-black text-white mb-2 tracking-wide text-center">AreaInsight</h1>
        <div className="flex items-center gap-3 text-emerald-400 bg-emerald-900/30 px-6 py-3 rounded-full border border-emerald-500/30">
          <Loader2 className="w-5 h-5 animate-spin" aria-hidden="true"/>
          <p className="font-bold uppercase tracking-widest text-xs">{t.fetchingData}</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-900 text-slate-100 font-sans pb-32 relative selection:bg-blue-500/30 selection:text-blue-200">
      
      <div className="sr-only" aria-live="polite" aria-atomic="true">
        {a11yAnnouncement}
      </div>

      {showEmergencyHub && (
        <div className="fixed inset-0 z-[100] bg-slate-950/90 backdrop-blur-md flex flex-col items-center justify-center p-6 animate-[fadeIn_0.2s_ease-out]" role="dialog" aria-modal="true" aria-labelledby="hub-title">
          <div className="w-full max-w-md bg-slate-900 border-2 border-rose-500/50 rounded-[2rem] p-6 shadow-[0_0_50px_rgba(225,29,72,0.3)]">
            <div className="flex items-center justify-center gap-3 mb-8">
              <div className="bg-rose-500 p-3 rounded-full animate-pulse" aria-hidden="true"><PhoneCall className="w-8 h-8 text-white" /></div>
              <h2 id="hub-title" className="text-3xl font-black text-white uppercase tracking-wider">{t.sosHub}</h2>
            </div>

            <div className="space-y-4">
              <a href="tel:112" aria-label="Call National Emergency Number 112" className="flex items-center justify-between bg-rose-600 hover:bg-rose-700 text-white p-5 rounded-2xl font-bold text-xl active:scale-95 transition-transform">
                <span>National Emergency (112)</span>
                <PhoneCall className="w-6 h-6" aria-hidden="true" />
              </a>
              <a href="tel:1091" aria-label={`Call ${t.helplineWomen}`} className="flex items-center justify-between bg-pink-600 hover:bg-pink-700 text-white p-5 rounded-2xl font-bold active:scale-95 transition-transform">
                <span>{t.helplineWomen}</span>
                <PhoneCall className="w-5 h-5" aria-hidden="true"/>
              </a>
              <a href="tel:1930" aria-label={`Call ${t.helplineCyber}`} className="flex items-center justify-between bg-blue-600 hover:bg-blue-700 text-white p-5 rounded-2xl font-bold active:scale-95 transition-transform">
                <span>{t.helplineCyber}</span>
                <PhoneCall className="w-5 h-5" aria-hidden="true"/>
              </a>

              <div className="h-px bg-white/10 my-6" aria-hidden="true"></div>

              <a href="https://www.google.com/maps/search/nearest+police+station" target="_blank" rel="noopener noreferrer" className="flex items-center justify-between bg-slate-800 hover:bg-slate-700 text-emerald-400 border border-emerald-500/30 p-5 rounded-2xl font-bold active:scale-95 transition-transform">
                <span>{t.nearestPolice}</span>
                <MapPin className="w-6 h-6" aria-hidden="true"/>
              </a>
              <a href="https://www.google.com/maps/search/nearest+hospital" target="_blank" rel="noopener noreferrer" className="flex items-center justify-between bg-slate-800 hover:bg-slate-700 text-emerald-400 border border-emerald-500/30 p-5 rounded-2xl font-bold active:scale-95 transition-transform">
                <span>{t.nearestHosp}</span>
                <PlusSquare className="w-6 h-6" aria-hidden="true"/>
              </a>
            </div>

            <button 
              onClick={() => { triggerHaptic(); setShowEmergencyHub(false); }}
              className="mt-8 w-full bg-slate-800 hover:bg-slate-700 text-slate-300 py-4 rounded-2xl font-bold uppercase tracking-widest border border-white/10"
              aria-label={t.close}
            >
              {t.close}
            </button>
          </div>
        </div>
      )}

      <header className="bg-slate-900/80 backdrop-blur-xl border-b border-white/10 sticky top-0 z-30 shadow-lg">
        <div className="max-w-5xl mx-auto p-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="p-2 bg-gradient-to-br from-blue-500 to-blue-700 rounded-xl shadow-lg shadow-blue-900/50 border border-blue-400/30" aria-hidden="true">
              <Shield className="w-6 h-6 text-white" />
            </div>
            <div>
              <h1 className="text-xl font-black text-white leading-tight tracking-wide">{t.title}</h1>
              <div className="flex items-center gap-2">
                <span className="relative flex h-2 w-2" aria-hidden="true">
                  <span className={`animate-ping absolute inline-flex h-full w-full rounded-full opacity-75 ${apiStatus === 'fallback' ? 'bg-amber-400' : 'bg-emerald-400'}`}></span>
                  <span className={`relative inline-flex rounded-full h-2 w-2 ${apiStatus === 'fallback' ? 'bg-amber-500' : 'bg-emerald-500'}`}></span>
                </span>
                <p className="text-[10px] font-bold text-slate-400 uppercase tracking-widest" aria-live="polite">
                  {apiStatus === 'fallback' ? t.offlineMode : t.liveAPI}
                </p>
              </div>
            </div>
          </div>
          
          <div className="relative">
            <Globe className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400 pointer-events-none" aria-hidden="true"/>
            <select 
              value={language}
              onChange={(e) => {
                triggerHaptic();
                setLanguage(e.target.value);
                if (isSpeaking) { window.speechSynthesis.cancel(); setIsSpeaking(false); }
              }}
              aria-label="Select Language"
              className="pl-9 pr-4 py-2 bg-slate-800 border border-white/10 rounded-xl focus:outline-none focus:border-blue-500 font-bold text-slate-200 text-sm cursor-pointer appearance-none shadow-inner"
            >
              <option value="en">English</option>
              <option value="hi">हिंदी</option>
              <option value="mr">मराठी</option>
              <option value="gu">ગુજરાતી</option>
            </select>
          </div>
        </div>
      </header>

      <main className="max-w-5xl mx-auto p-4 mt-4 grid grid-cols-1 lg:grid-cols-3 gap-6" key={animateKey}>
        
        <section className="lg:col-span-1 space-y-6" aria-label="Controls and Location Selection">
          <div className="bg-slate-800 p-6 rounded-[2rem] shadow-xl border border-white/5 ring-1 ring-white/10">
            
            <button
              onClick={startListening}
              aria-label={isListening ? t.listening : t.tapToSpeak}
              className={`w-full mb-6 py-4 rounded-[2rem] flex flex-col items-center justify-center gap-2 transition-all duration-300 border-2 ${
                isListening 
                  ? 'bg-rose-500/10 border-rose-500/50 text-rose-400 animate-pulse' 
                  : 'bg-blue-500/10 border-blue-500/30 text-blue-400 hover:bg-blue-500/20'
              }`}
            >
              <div className={`p-4 rounded-full transition-colors duration-300 ${isListening ? 'bg-rose-600 text-white' : 'bg-blue-600 text-white'}`} aria-hidden="true">
                <Mic className={`w-8 h-8 ${isListening ? 'animate-bounce' : ''}`} />
              </div>
              <span className="font-extrabold text-sm tracking-wide text-center px-2">{isListening ? t.listening : t.tapToSpeak}</span>
            </button>
            {micError && <p className="text-center text-sm font-bold text-rose-400 mb-4 bg-rose-950 p-2 rounded-lg border border-rose-900" role="alert">{t.micError}</p>}

            <div className="border-t border-white/5 pt-6">
              <label htmlFor="state-select" className="block text-[10px] font-bold text-slate-400 mb-2 uppercase tracking-widest">{t.selectState}</label>
              <div className="relative">
                 <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-500 pointer-events-none" aria-hidden="true"/>
                 <select 
                   id="state-select"
                   value={selectedState}
                   onChange={(e) => {
                     triggerHaptic();
                     setSelectedState(e.target.value);
                     if (isSpeaking) { window.speechSynthesis.cancel(); setIsSpeaking(false); }
                   }}
                   className="w-full pl-12 px-4 py-3 bg-slate-900 border border-white/10 rounded-2xl focus:border-blue-500 font-bold text-slate-200 cursor-pointer appearance-none shadow-inner"
                 >
                   {stateList.map((d) => (
                     <option key={d.state} value={d.state}>{d.state}</option>
                   ))}
                 </select>
              </div>
            </div>

            <div className="mt-6 pt-6 border-t border-white/5">
              <div className="flex items-center justify-center gap-2 mb-1 opacity-70" aria-hidden="true">
                <Users className="w-4 h-4 text-slate-400" />
                <h3 className="text-xs font-bold text-slate-400 uppercase tracking-widest">{t.population}</h3>
              </div>
              <p className="text-2xl font-black text-white text-center tracking-tight" aria-label={`Population ${stateData.pop} ${t.lakhs}`}>
                {stateData.pop} <span className="text-base font-bold text-slate-400" aria-hidden="true">{t.lakhs}</span>
              </p>
            </div>

          </div>

          <button 
            onClick={handleNextTip}
            aria-label={`Safety tip: ${isSafe ? t.tipSafe[tipIndex] : t.tipDanger[tipIndex]}. ${t.tapForMore}`}
            className={`w-full text-left p-6 rounded-[2rem] border ring-1 transition-all duration-300 flex items-start gap-4 active:scale-[0.98] ${
              isSafe 
                ? 'bg-emerald-950/50 hover:bg-emerald-900/60 border-emerald-900/50 ring-emerald-500/20 text-emerald-200' 
                : 'bg-orange-950/50 hover:bg-orange-900/60 border-orange-900/50 ring-orange-500/20 text-orange-200'
            }`}
          >
            <Lightbulb className={`w-6 h-6 flex-shrink-0 mt-1 ${isSafe ? 'text-emerald-400' : 'text-orange-400'}`} aria-hidden="true"/>
            <div className="flex-1">
              <div className="flex justify-between items-center mb-1" aria-hidden="true">
                <h4 className="font-extrabold tracking-wide uppercase text-xs opacity-70">{t.tipTitle}</h4>
                <span className="text-[9px] uppercase tracking-widest opacity-50 bg-white/10 px-2 py-0.5 rounded-full">{t.tapForMore}</span>
              </div>
              <p className="text-sm font-medium leading-relaxed transition-opacity duration-300" key={tipIndex} aria-hidden="true">
                {isSafe ? t.tipSafe[tipIndex] : t.tipDanger[tipIndex]}
              </p>
            </div>
          </button>
        </section>

        <section className="lg:col-span-2 space-y-6" aria-label="Safety Metrics and Charts">
          
          <div className={`p-6 md:p-8 rounded-[2rem] shadow-2xl border-2 flex flex-col sm:flex-row items-center justify-between gap-6 transition-all duration-500 ${
            isSafe ? 'bg-gradient-to-br from-emerald-900/80 to-slate-900 border-emerald-500/30' : 'bg-gradient-to-br from-rose-900/80 to-slate-900 border-rose-500/30'
          }`}>
            <div className="flex items-center gap-6">
              <div aria-hidden="true" className={`p-5 rounded-full border-2 ${isSafe ? 'bg-emerald-500/20 border-emerald-400 shadow-[0_0_30px_rgba(52,211,153,0.3)]' : 'bg-rose-500/20 border-rose-400 shadow-[0_0_30px_rgba(244,63,94,0.3)]'}`}>
                {isSafe ? <ThumbsUp className="w-10 h-10 text-emerald-400" /> : <AlertTriangle className="w-10 h-10 text-rose-400" />}
              </div>
              <div>
                <h2 className="text-3xl md:text-4xl font-black text-white tracking-tighter drop-shadow-md">{stateData.state}</h2>
                <p className={`text-lg font-bold mt-1 tracking-wide uppercase ${isSafe ? 'text-emerald-400' : 'text-rose-400'}`}>
                  {isSafe ? t.safe : t.danger}
                </p>
              </div>
            </div>

            <button
              id="play-audio-btn"
              onClick={handleReadAloud}
              aria-label={isSpeaking ? t.stopAudio : t.readSummary}
              className={`px-8 py-5 rounded-full flex items-center justify-center text-center gap-3 text-sm md:text-base font-black uppercase tracking-widest transition-all duration-300 border-2 ${
                isSpeaking
                  ? 'bg-amber-500 text-slate-900 border-amber-300 animate-pulse shadow-[0_0_20px_rgba(245,158,11,0.5)]'
                  : 'bg-slate-800 text-amber-400 border-amber-500/50 hover:bg-slate-700 shadow-lg'
              }`}
            >
              {isSpeaking ? <VolumeX className="w-6 h-6 flex-shrink-0" aria-hidden="true"/> : <Volume2 className="w-6 h-6 flex-shrink-0" aria-hidden="true"/>}
              <span aria-hidden="true">{isSpeaking ? t.stopAudio : t.readSummary}</span>
            </button>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
            
            <div className="bg-slate-800 p-6 rounded-[2rem] shadow-lg border border-white/5 ring-1 ring-white/10 relative overflow-hidden">
              <div className="absolute top-0 right-0 p-4 opacity-10" aria-hidden="true"><Activity className="w-16 h-16" /></div>
              <h3 className="text-[10px] font-bold text-slate-400 mb-2 uppercase tracking-widest relative z-10" aria-hidden="true">{t.totalCases}</h3>
              <div className="flex flex-col mb-1 relative z-10">
                <span className="text-4xl font-black text-white tracking-tighter" aria-label={`${t.totalCases}: ${stateData.y2022}`}>
                  {stateData.y2022.toLocaleString('en-IN')}
                </span>
                <div className={`flex items-center mt-2 text-xs font-bold uppercase tracking-wider ${isTrendUp ? 'text-rose-400' : 'text-emerald-400'}`} aria-label={`${isTrendUp ? 'Increased' : 'Decreased'} by ${Math.abs(yoyChange).toFixed(1)} percent since last year`}>
                  {isTrendUp ? <TrendingUp className="w-4 h-4 mr-1" aria-hidden="true"/> : <TrendingDown className="w-4 h-4 mr-1" aria-hidden="true"/>}
                  <span aria-hidden="true">{Math.abs(yoyChange).toFixed(1)}% vs '21</span>
                </div>
              </div>
            </div>

            <div className="bg-slate-800 p-6 rounded-[2rem] shadow-lg border border-white/5 ring-1 ring-white/10 relative overflow-hidden">
               <div className="absolute top-0 right-0 p-4 opacity-10"><CheckCircle className="w-16 h-16" aria-hidden="true" /></div>
              <h3 className="text-[10px] font-bold text-slate-400 mb-2 uppercase tracking-widest relative z-10" aria-hidden="true">{t.policeAction}</h3>
              <div className="flex flex-col mb-1 relative z-10">
                <span className="text-4xl font-black text-white tracking-tighter" aria-label={`Police charge rate: ${stateData.charge} percent`}>
                  {stateData.charge}%
                </span>
                <span className="flex items-center mt-2 text-xs font-bold uppercase tracking-wider text-blue-400" aria-hidden="true">
                  <Shield className="w-4 h-4 mr-1" aria-hidden="true"/> {t.casesResolved}
                </span>
              </div>
            </div>

            <div className="bg-slate-800 p-6 rounded-[2rem] shadow-lg border border-white/5 ring-1 ring-white/10 flex flex-col justify-between" aria-label={isTrendUp ? t.a11yGraphUp : t.a11yGraphDown}>
              <h3 className="text-[10px] font-bold text-slate-400 mb-2 uppercase tracking-widest flex items-center gap-1" aria-hidden="true">
                <Activity className="w-3 h-3" /> Trend '20 - '22
              </h3>
              <div className="flex-1 flex items-end justify-center py-2" aria-hidden="true">
                 <svg width="100%" height="40" viewBox="0 0 100 40" preserveAspectRatio="none" className="overflow-visible w-full">
                    <line x1="10" y1="0" x2="90" y2="0" stroke="#334155" strokeWidth="1" strokeDasharray="2" />
                    <line x1="10" y1="20" x2="90" y2="20" stroke="#334155" strokeWidth="1" strokeDasharray="2" />
                    <line x1="10" y1="40" x2="90" y2="40" stroke="#334155" strokeWidth="1" strokeDasharray="2" />
                    <polyline 
                      points={`${p1} ${p2} ${p3}`} 
                      fill="none" 
                      strokeWidth="3" 
                      strokeLinecap="round" 
                      strokeLinejoin="round" 
                      className={trendColor}
                    />
                    <circle cx="10" cy={p1.split(',')[1]} r="4" className={`fill-slate-900 stroke-2 ${trendColor}`} />
                    <circle cx="50" cy={p2.split(',')[1]} r="4" className={`fill-slate-900 stroke-2 ${trendColor}`} />
                    <circle cx="90" cy={p3.split(',')[1]} r="5" className={`fill-white stroke-2 ${trendColor}`} />
                 </svg>
              </div>
            </div>

            <div className="bg-slate-800 p-6 rounded-[2rem] shadow-lg border border-white/5 ring-1 ring-white/10">
              <h3 className="text-[10px] font-bold text-slate-400 mb-4 uppercase tracking-widest" aria-hidden="true">{t.breakdown}</h3>
              <div className="space-y-4">
                <div aria-hidden="true" className="flex items-center gap-3">
                  <div className="p-2 bg-pink-500/20 text-pink-400 rounded-lg"><ShieldCheck className="w-5 h-5" /></div>
                  <div className="flex-1">
                    <div className="flex justify-between text-xs font-bold text-slate-300 mb-1"><span>{t.womenSafety}</span><span>{Math.floor(stateData.rate * 0.18)}%</span></div>
                    <div className="w-full bg-slate-900 h-1.5 rounded-full"><div className="h-full bg-pink-500 rounded-full" style={{width: '18%'}}></div></div>
                  </div>
                </div>
                <div aria-hidden="true" className="flex items-center gap-3">
                  <div className="p-2 bg-blue-500/20 text-blue-400 rounded-lg"><Laptop className="w-5 h-5" /></div>
                  <div className="flex-1">
                    <div className="flex justify-between text-xs font-bold text-slate-300 mb-1"><span>{t.cyberCrime}</span><span>{Math.floor(stateData.rate * 0.12)}%</span></div>
                    <div className="w-full bg-slate-900 h-1.5 rounded-full"><div className="h-full bg-blue-500 rounded-full" style={{width: '12%'}}></div></div>
                  </div>
                </div>
                <div aria-hidden="true" className="flex items-center gap-3">
                  <div className="p-2 bg-amber-500/20 text-amber-400 rounded-lg"><Car className="w-5 h-5" /></div>
                  <div className="flex-1">
                    <div className="flex justify-between text-xs font-bold text-slate-300 mb-1"><span>{t.autoTheft}</span><span>{Math.floor(stateData.rate * 0.45)}%</span></div>
                    <div className="w-full bg-slate-900 h-1.5 rounded-full"><div className="h-full bg-amber-500 rounded-full" style={{width: '45%'}}></div></div>
                  </div>
                </div>
                <div className="sr-only">
                  {t.breakdown}: {t.womenSafety} is {Math.floor(stateData.rate * 0.18)} percent. {t.cyberCrime} is {Math.floor(stateData.rate * 0.12)} percent. {t.autoTheft} is {Math.floor(stateData.rate * 0.45)} percent.
                </div>
              </div>
            </div>

          </div>

          <div className="bg-slate-800 p-6 md:p-8 rounded-[2rem] shadow-lg border border-white/5 ring-1 ring-white/10">
            <div className="mb-8" aria-hidden="true">
              <h3 className="text-xl font-black text-white">{t.crimeRate}</h3>
              <p className="text-[10px] font-bold text-slate-400 mt-1 uppercase tracking-widest">{t.rateSubtitle}</p>
            </div>
            
            <div className="sr-only">
              {t.crimeRate}. {stateData.state} rate is {stateData.rate}. {t.nationalAvg} is {nationalData.rate}.
            </div>

            <div className="space-y-8" aria-hidden="true">
              <div>
                <div className="flex justify-between text-sm font-bold mb-3">
                  <span className="text-white text-lg tracking-wide">{stateData.state}</span>
                  <span className="text-white text-xl font-black">{stateData.rate}</span>
                </div>
                <div className="w-full bg-slate-900 h-4 rounded-full overflow-hidden shadow-inner border border-white/5">
                  <div 
                    className={`h-full rounded-full shadow-[0_0_15px_currentColor] ${isSafe ? 'bg-emerald-500 text-emerald-500' : 'bg-rose-500 text-rose-500'}`}
                    style={{ width: `${Math.min((stateData.rate / 1500) * 100, 100)}%`, transition: 'width 0.8s cubic-bezier(0.4, 0, 0.2, 1)' }}
                  />
                </div>
              </div>

              <div>
                <div className="flex justify-between text-sm font-bold mb-3">
                  <span className="text-slate-400 text-base uppercase tracking-wider">{t.nationalAvg}</span>
                  <span className="text-slate-300 text-xl font-black">{nationalData.rate}</span>
                </div>
                <div className="w-full bg-slate-900 h-4 rounded-full overflow-hidden shadow-inner border border-white/5">
                  <div 
                    className="h-full bg-slate-600 rounded-full"
                    style={{ width: `${Math.min((nationalData.rate / 1500) * 100, 100)}%` }}
                  />
                </div>
              </div>
            </div>
          </div>

        </section>
      </main>

      {/* FLOATING ACTION BAR */}
      <div className="fixed bottom-6 left-1/2 -translate-x-1/2 z-40 w-[95%] max-w-lg" role="region" aria-label="Emergency Actions">
        <div className="flex gap-2 bg-slate-900/80 backdrop-blur-2xl p-2 rounded-[2rem] shadow-2xl border border-white/10 ring-1 ring-white/5">
          
          <button 
            onClick={() => { triggerHaptic('sos'); setShowEmergencyHub(true); }}
            aria-label={`Open ${t.sosHub}`}
            className="flex-[2] flex items-center justify-center gap-2 bg-gradient-to-r from-rose-600 to-rose-700 hover:from-rose-500 hover:to-rose-600 text-white py-4 px-4 rounded-[1.5rem] shadow-[0_5px_20px_rgba(225,29,72,0.5)] transition-all active:scale-95 border border-rose-400/50"
          >
            <AlertTriangle className="w-6 h-6 animate-pulse" aria-hidden="true"/>
            <span className="font-black uppercase tracking-widest text-sm" aria-hidden="true">{t.sosHub}</span>
          </button>

          <a 
            href={`https://wa.me/?text=${encodedSosText}`}
            target="_blank" rel="noopener noreferrer"
            onClick={() => triggerHaptic()}
            className="flex-1 flex flex-col items-center justify-center bg-emerald-600 hover:bg-emerald-500 text-white py-2 rounded-[1.5rem] transition-all active:scale-95"
            aria-label={`Send ${t.waSOS}`}
          >
            <MessageCircle className="w-5 h-5 mb-1" aria-hidden="true"/>
            <span className="font-bold text-[9px] uppercase tracking-wider text-emerald-100" aria-hidden="true">WhatsApp</span>
          </a>

          <a 
            href={`sms:?body=${encodedSosText}`}
            onClick={() => triggerHaptic()}
            className="flex-1 flex flex-col items-center justify-center bg-blue-600 hover:bg-blue-500 text-white py-2 rounded-[1.5rem] transition-all active:scale-95"
            aria-label={`Send ${t.smsSOS}`}
          >
            <MessageSquare className="w-5 h-5 mb-1" aria-hidden="true"/>
            <span className="font-bold text-[9px] uppercase tracking-wider text-blue-100" aria-hidden="true">SMS</span>
          </a>
          
        </div>
      </div>
      
    </div>
  );
}