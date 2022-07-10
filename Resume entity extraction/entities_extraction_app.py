from flask import Flask, jsonify, request
import re
import string as string
import re
from collections import OrderedDict
import string
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop = stopwords.words('english')
from nltk.corpus import wordnet
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.downloader.download('maxent_ne_chunker')
nltk.downloader.download('words')
nltk.downloader.download('treebank')
nltk.downloader.download('maxent_treebank_pos_tagger')
import warnings
warnings.filterwarnings("ignore")


skills = {'microsoft word', 'data analysis', 'transformers', 'numpy', 'numpy', 'ms sql', 'natural language processing', 'tensorflow and keras',
          'sql', 'sql server', 'css', 'javascript', 'spyder', 'pytorch', 'tableau', 'perl', 't-sql', 'machine learning', 'c++', 'c language', 'c program', 'c programming',
          'data science', 'aws', 'excel', 'c#.net', 'anaconda', 'scikit learn', 'seaborn', 'visual basic.net', 'python', 'oracle', 'db2',
          'html', 'php', 'pandas', 'word', 'aws ec2', 'python (ide)', 'java', 'keras','microsoft office', 'nlp', 'ruby', 'power bi', 'matplotlib',
          'data visualizations', 'aws lambda', 'postgres sql', 'mysql', 'tensorflow', 'jupyter',"c++", "sql", "python", "java", "r language", "facebook", "html", "ladder", "javascript", "servers", "network security", "big data", "algorithms", 
          "spark", "sas", "artificial intelligence", "ruby", "algorithms", "analytical skills", "big data", "compiling statistics",
          "data analytics", "data mining", "database design", "database management", 'Neural Networks', 
          "quantitative research", "quantitative reports", "statistical analysis",  "computing", 
          "customer support", "debugging", "design",  "html","information technology", 
          "network architecture", "network security", "networking", "operating systems", "programming", 
          "systems analysis", "technical support", "testing", "search engine optimization", "web analytics", "automated marketing software",
          "subject matter experts","microsoft office",  "customer relationship management", "cloud/saas services", "database management",
          "telecommunications", "human resources software", "enterprise resource planning software", "database software", "query software",
          "medical coding", "sonography", "structural analysis", "artificial intelligence", 
          "ms office", "ms word",  "ms excel", "ms powerpoint",  "ms outlook",  "ms access", "ms onenote",
          "google drive",  "google docs", "google sheets", "google forms", "google slides", "writing",  "wordpress", "seo",
          "spreadsheets",  "excel",  "google sheets",  "openoffice", "comparative analyses", "pivot tables",  "macros", "link to database",
          "graphical photoshop",  "illustrator, indesign", "acrobat", "corel draw", "web", "deep learning", ".net"
          'neural networks','seaborn','scrpay','tessract','opencv, computer vision, cv','pyspyder', 'eda', 'exploratory data analysis', 'jyputer notebook',
          'anaconda','pycharm', 'google colab, colab', 'vs code', 'heroku', 'matlab, matlab', 's3', 'sqs', 'arduino, raspberry pi', 'oops','photoshop',
          'nodejs, nodejs', 'reactjs', 'expressjs', 'ms access', 'generative adversial network, gan', 'mongo db', 'visual studio', 'ms excel', 'ms access',
          'ms word', 'ms powerpoint', 'idle', 'python 3.4', 'python 3.6', 'python 2.6', 'python 3.7', 'linear regression', 'regression algorithms', 'logistic regression',
          'random forest', 'decision trees', 'ada boost,', 'gradient boost', 'knn','k means clustering', 'density based clustering', 'hierarchal clustering', 'naive bayes', 
          'support vector machines', 'xg boost', 'pca', 'tsne' ,'time series', 'alexnet', 'vggnet', 'residual network, inception', 'network,rnn & lstm', 'rcnn',
          'tfod framework', 'android', 'algo & ds', 'data structures and alogorithm','data structures', 'qt creator', 'github,', 'quantum gis' 'mathematical modeling', 'statistical modeling,','hadoop,mapreduce', 
          "rcnn",'alexanet','resnet','deepar','pca','aws sagemaker', 'seo', 'sem', 'mailchimp', 'wordpress', 'wix', 'hubspot',
          'Marketing Strategy','Competitor Analysis', 'Social Media Marketing', 'Search Engine Optimization', 'Search Engine Management', 'Web based Analytics',
          'Search Marketing, Social Media', 'Marketing, App Promotion, Video', 'Advertising & Data Analytics', 'SEM (Google Ads, Bing Ads), SMM (Facebook Advertisement) and SEO',
          'Re-marketing (Static & Dynamic)', 'Brand Promotion', 'Budget Allocation', 'Product listing ads', 'A/B Split Testing', 'Lead Generation', 'Analysis and Reporting (Google Analytics & Google Ads Reporting)',
          'Amazon Sponsored Ads', 'Facebook Ads', 'Google Ads', 'ORM', 'Brand Development', 'Political Campaign', 'Website Designing', 'Marketing Strategy',
          'SEO', 'Team Leader','Sales& BD Ops, Strategy, Marketing', 'Automate Marketing & Prospecting', 'Secondary Market Research', 'Business Analytics/BI/Reports', 'Technical Delivery (SDLC, Agile)',
          'Communication(Hindi, English)', 'Leadership', 'Problem Solving', 'Resilience', 'Persistence', 'Public Speaking', 'Teamwork',
          'python', 'bash', 'sql', 'opencv', 'spacy', 'nltk', 'scikit-learn', 'numpy', 'pandas', 'selenium', 'beautiful soup', 'image processing', 'image augmentation', 'object detection', 'image classification',
          'rnns', 'grus', 'lstms','sentiment analysis','named entity recognition (ner)', 'text classification', 'nvidia tlt-kit', 'deepstream', 'jetson' , 'nano device',
          'analytical ability','adaptability','critical thinking','decision making','devising strategic plans to expand sales','swot analysis','scenario planning','project management',
          'sales forecasting','teamwork','attention management','tracking industry trends','marketing','creativity communication','client management content writing','resiliency time management',
          'team player leadership','relationship building','consumer engagement team management','social media campaign building'}
      

education_dict = {'master in computer application','masters in computer application','master in computer science', 'masters in computer science', 'bachelors in computer science', 'bachelor of computer science',
                'bachelor in computer science','bachelors of computer science', 'bachelor of arts in history', 'bachelors of arts in history','bachelor in arts history','bachelor of arts in english',
                'bachelors of arts in english', 'bachelors of arts in economics', 'bachelor of arts in economics', 'bachelors of arts in political science', 'bachelor of arts in political science',
                'bachelor of arts in psychology','bachelors of arts in psychology','bachelors of arts in literature language and linguistics','bachelor of arts in literature language and linguistics',
                'bachelor of arts hons in fine arts', 'master of computer science', 'masters of computer science', 'bachelors in history','bachelor in history','bachelors in english','bachelor in english',
                'bachelors in economics','bachelor in economics','bachelors in political science','bachelor in political science','bachelors in psychology','bachelor in psychology','bachelors in literature language and linguistics',
                'bachelor in literature language and linguistics','ba in literature language and linguistics','ba history','ba/ba fine arts','ba economics','ba journalism','ba psychology','ba political science' 
                'ba llb','ba in history','ba in fine arts','ba in economics','ba in journalism','ba in psychology','ba in political science', 'ba in llb','bachelors of business administration','bachelor of business administration',
                'bachelors in business administration','bachelor in business administration','bachelor of science in physics','bachelors of science in physics','bachelor in  physics','bachelors in  physics',
                'bachelors of science in chemistry','bachelor of science in chemistry','bachelors in chemistry','bachelor in chemistry','bachelors of science in botany','bachelor of science in botany',
                'bachelors in botany','bachelor in botany','bachelors of science in information technology','bachelor of science in information technology','bachelors in information technology','bachelor in information technology',
                'bachelors of science in statistics','bachelor of science in statistics','bachelors in statistics','bachelor in statistics','bachelors of science in mathematics','bachelor of science in mathematics',
                'bachelors in mathematics','bachelor in mathematics','bachelors of science in zoology','bachelor of science in zoology','bachelors in zoology','bachelor in zoology','bachelors of science in agriculture',
                'bachelor of science in agriculture','bachelors in agriculture','bachelor in agriculture','bachelors of science in biotechnology','bachelor of science in biotechnology','bachelors in biotechnology',
                'bachelor in biotechnology','bachelors of science in microbiology','bachelor of science in microbiology','bachelors in microbiology','bachelor in microbiology','bachelors of science in nursing',
                'bachelor of science in nursing','bachelors in nursing','bachelor in nursing','bachelors of science in data science','bachelor of science in data science','bachelors in data science','bachelor in data science',
                'bsc agriculture','bsc biotechnology','bsc zoology','bsc clinical research and healthcare management','bsc forestry','bsc microbiology','bsc nursing','bsc physiotherapy','bsc radiology','bsc bioinformatics',
                'bsc physics','bsc chemistry','bsc botany','bsc it','bsc computer science','bsc data science','bsc in agriculture','bsc in biotechnology','bsc in zoology','bsc in clinical research and healthcare management',
                'bsc in forestry','bsc in microbiology','bsc in nursing','bsc in physiotherapy','bsc in radiology','bsc in bioinformatics','bsc in physics','bsc in chemistry','bsc in botany','bsc in it','bsc in computer science',
                'bsc in data science','masters in history','master in history','masters in english','master in english','msc in botany','msc in it','msc in computer science','msc in data science',
                'masters in economics','bachelor in economics','masters in political science','master in political science','masters in psychology','master in psychology','masters in literature language and linguistics',
                'master in literature language and linguistics','ma in literature language and linguistics','ma history','ma fine arts','ma economics','ma journalism','ma psychology','ma political science' ,
                'ma llb','ba in history','ma in fine arts','ma in economics','ma in journalism','ma in psychology','ma in political science', 'ma in llb','masters of business administration','master of business administration',
                'masters in business administration','master in business administration','master of science in physics','masters of science in physics','master in  physics','masters in  physics',
                'masters of science in chemistry','master of science in chemistry','masters in chemistry','master in chemistry','masters of science in botany','master of science in botany',
                'masters in botany','bachelor in botany','masters of science in information technology','master of science in information technology','masters in information technology','master in information technology',
                'masters of science in statistics','master of science in statistics','masters in statistics','master in statistics','masters of science in mathematics','master of science in mathematics',
                'masters in mathematics','master in mathematics','masters of science in zoology','master of science in zoology','masters in zoology','master in zoology','masters of science in agriculture',
                'master of science in agriculture','masters in agriculture','master in agriculture','masters of science in biotechnology','master of science in biotechnology','master in biotechnology',
                'master in biotechnology','masters of science in microbiology','master of science in microbiology','masters in microbiology','master in microbiology','master of science in nursing',
                'master of science in nursing','masters in nursing','master in nursing','masters of science in data science','master of science in data science','masters in data science','master in data science',
                'msc agriculture','msc biotechnology','msc zoology','msc clinical research and healthcare management','msc forestry','msc microbiology','msc nursing','msc physiotherapy','msc radiology','msc bioinformatics',
                'msc physics','msc chemistry','msc botany','msc it','msc computer science','msc data science','msc in agriculture','msc in biotechnology','msc in zoology','msc in clinical research and healthcare management',
                'msc in forestry','msc in microbiology','msc in nursing','msc in physiotherapy','msc in radiology','msc in bioinformatics','msc in physics','msc in chemistry',
                'bachelor of arts in hons in hindi journalism and mass communication', 'bachelors of arts in hons in hindi journalism and mass communication','bachelors in hons in hindi journalism and mass communication',
                'bachelor in hons in hindi journalism and mass communication','ba in hons in hindi journalism and mass communication','ba hons in hindi journalism and mass communication',
                'bachelor of arts in flim making and mass communication', 'bachelors of arts in flim making and mass communication','bachelors in flim making and mass communication',
                'bachelor in flim making and mass communication','ba in flim making and mass communication','ba flim making and mass communication','bachelors in mass communication',
                'bachelor of arts in hons journalism and mass communication', 'bachelors of arts in hons journalism and mass communication','bachelors in hons journalism and mass communication',
                'bachelor in hons journalism and mass communication','ba in hons journalism and mass communication','ba hons journalism and mass communication',
                'bachelor of arts in mass media', 'bachelors of arts in mass media','bachelors in mass media','bachelor in mass media','ba in history','ba mass media',
                'master of arts in hons in hindi journalism and mass communication', 'masters of arts in hons in hindi journalism and mass communication','masters in hons in hindi journalism and mass communication',
                'master in hons in hindi journalism and mass communication','ma in hons in hindi journalism and mass communication','ma hons in hindi journalism and mass communication',
                'master of arts in flim making and mass communication', 'masters of arts in flim making and mass communication','masters in flim making and mass communication',
                'master in flim making and mass communication','ma in flim making and mass communication','ma flim making and mass communication',
                'master of arts in hons journalism and mass communication', 'masters of arts in hons journalism and mass communication','masters in hons journalism and mass communication',
                'master in hons journalism and mass communication','ma in hons journalism and mass communication','ma hons journalism and mass communication',
                'master of arts in mass media', 'masters of arts in mass media','masters in mass media','master in mass media','ma in history','ma mass media',
                'bachelors of science in mass communication and journalism','bachelor of science in mass communication and journalism','bachelors in mass communication and journalism',
                'master in mass communication and journalism','bsc mass communication and journalism', 'bcs in mass communication and journalism','pgdm in business journalism and corporate communication',
                'masters of science in mass communication and journalism','master of science in mass communication and journalism','masters in mass communication and journalism',
                'bachelor of management science', 'bachelors of management science','bachelor of event management','bachelors of event management',
                'bachelor of management social work', 'bachelors of management social work','bachelor of business studies', 'bachelors of business studies',
                'master of management science', 'masters of management science','master of event management','masters of event management',
                'master of management social work', 'masters of management social work','master of business studies', 'masters of business studies',
                'master in mass communication and journalism','bsc mass communication and journalism', 'bcs in mass communication and journalism','post graduate diploma in business journalism and corporate communication',
                'bachelors of technology in aeronautical engineering','bachelor of technology in aeronautical engineering','b.tech aeronautical engineering','btech aeronautical engineering','b.tech ai','btech ai',
                'bachelors of technology in automobile engineering','bachelor of technology in automobile engineering','b.tech automobile engineering','btech automobile engineering','b.tech ae','btech ae',
                'bachelors of technology in biotechnology','bachelor of technology in biotechnology','b.tech biotechnology','btech biotechnology','b.tech biotech','btech biotech',
                'bachelors of technology in civil engineering','bachelor of technology in civil engineering','b.tech civil engineering','btech civil engineering','b.tech civil','btech civil',
                'bachelors of technology in computer science and engineering','bachelor of technology in computer science and engineering','b.tech computer science and engineering','btech computer science and engineering','b.tech cse','btech cse',
                'bachelors of technology in electrical and electronics engineering','bachelor of technology in electrical and electronics engineering','b.tech electrical and electronics engineering','btech eee','b.tech eee','btech eee',
                'bachelors of technology in mechanical engineering','bachelor of technology in mechanical engineering','b.tech mechanical engineering','btech mech','b.tech mech','btech mech',
                'bachelors of technology in electronics & communication','bachelor of technology in electronics & communication','b.tech electronics & communication','btech ec','b.tech ec','btech ec',
                'bachelors of technology in cse with specialization in artificial intelligence and machine learning','bachelor of technology in cse with specialization in artificial intelligence and machine learning',
                'b.tech cse with specialization in artificial intelligence and machine learning','btech cse with ai','b.tech cse with ai','btech cse with ai',
                'bachelors of technology in cse with specialization in cloud computing','bachelor of technology in cse with cloud computing',
                'b.tech cse with specialization in cloud computing','btech cse with iot','b.tech cse with iot','btech cse with iot',
                'bachelors of technology in information technology','bachelor of technology in information technology','b.tech information technology','btech cinformation technology','b.tech it','btech it',
                'bachelors of technology in cse with specialization in cyber security','bachelor of technology in cse with cyber security',
                'bachelor of technology in cse with specialization in cyber security','bachelors of technology in cse with cyber security',
                'b.tech cse with specialization in cyber security ','btech cse with cyber security','b.tech cse with cyber security','btech cse with cyber security',
                'masters of technology in aeronautical engineering','master of technology in aeronautical engineering','m.tech aeronautical engineering','mtech aeronautical engineering','m.tech ai','mtech ai',
                'masters of technology in automobile engineering','master of technology in automobile engineering','m.tech automobile engineering','mtech automobile engineering','m.tech ae','mtech ae',
                'masters of technology in biotechnology','master of technology in biotechnology','m.tech biotechnology','mtech biotechnology','m.tech biotech','mtech biotech',
                'masters of technology in civil engineering','master of technology in civil engineering','m.tech civil engineering','mtech civil engineering','m.tech civil','mtech civil',
                'masters of technology in computer science and engineering','master of technology in computer science and engineering','m.tech computer science and engineering','mtech computer science and engineering','m.tech cse','btech cse',
                'masters of technology in electrical and electronics engineering','master of technology in electrical and electronics engineering','m.tech electrical and electronics engineering','mtech eee','m.tech eee','btech eee',
                'masters of technology in mechanical engineering','master of technology in mechanical engineering','m.tech mechanical engineering','mtech mech','m.techmech','mtech mech',
                'masters of technology in electronics & communication','master of technology in electronics & communication','m.tech electronics & communication','mtech ec','m.tech ec','mtech ec',
                'masters of technology in cse with specialization in artificial intelligence and machine learning','master of technology in cse with specialization in artificial intelligence and machine learning',
                'm.tech cse with specialization in artificial intelligence and machine learning','mtech cse with ai','m.tech cse with ai','mtech cse with ai',
                'masters of technology in cse with specialization in cloud computing','master of technology in cse with cloud computing',
                'm.tech cse with specialization in cloud computing','mtech cse with iot','m.tech cse with iot','mtech cse with iot',
                'masters of technology in information technology','master of technology in information technology','m.tech information technology','mtech cinformation technology','m.tech it','mtech it',
                'masters of technology in cse with specialization in cyber security','master of technology in cse with cyber security',
                'master of technology in cse with specialization in cyber security','masters of technology in cse with cyber security',
                'm.tech cse with specialization in cyber security ','m.tech cse with cyber security','m.tech cse with cyber security','mtech cse with cyber security',
                'bachelors of technology in electronics & communication engineering','bachelor of technology in electronics & communication engineering','b.tech electronics & communication engineering','btech electronics & communication engineering','m.tech ece','mtech ece',
                'masters of technology in electronics & communication engineering','master of technology in electronics & communication engineering','m.tech electronics & communication engineering','mtech electronics & communication engineering','m.tech ece','mtech ece',
                'bachelors of engineering in aeronautical engineering', 'bachelor of engineering in aeronautical engineering', 'be in aeronautical engineering ', 'be aeronautical engineering',
                'bachelors of engineering in automobile engineering', 'bachelor of engineering in automobile engineering', 'be in automobile engineering ', 'be automobile engineering',
                'bachelors of engineering in biotechnology', 'bachelor of engineering in biotechnology', 'be in biotechnology ', 'be biotechnology',
                'bachelors of engineering in computer science and engineering', 'bachelor of engineering in computer science and engineering', 'be in cse ', 'be cse','be in computer science and engineering','be computer science and engineering',
                'bachelors of engineering in information technology', 'bachelor of engineering in information technology', 'be in information technology', 'be information technology','be in it',
                'bachelors of engineering in mechanical engineering', 'bachelor of engineering in mechanical engineering', 'be in mechanical engineering ', 'be mechanical engineering','be mech',
                'bachelors of engineering in  electrical and electronics engineering', 'bachelor of engineering in  electrical and electronics engineering', 'be in  electrical and electronics engineering ', 'be  electrical and electronics engineering','be in eee','be eee',
                'bachelors of engineering in electronics & communication engineering', 'bachelor of engineering in electronics & communication engineering', 'be in electronics & communication engineering ', 'be electronics & communication engineeringg', 'be in ece','be ece',
                'masters of engineering in aeronautical engineering', 'master of engineering in aeronautical engineering', 'me in aeronautical engineering ', 'me aeronautical engineering',
                'masters of engineering in automobile engineering', 'master of engineering in automobile engineering', 'me in automobile engineering ', 'me automobile engineering',
                'masters of engineering in biotechnology', 'master of engineering in biotechnology', 'me in biotechnology ', 'me biotechnology','masters in technology','masters in science',
                'masters of engineering in computer science and engineering', 'master of engineering in computer science and engineering', 'me in cse ', 'me cse','me in computer science and engineering','me computer science and engineering',
                'masters of engineering in information technology', 'master of engineering in information technology', 'me in information technology', 'me information technology','me in it',
                'masters of engineering in mechanical engineering', 'master of engineering in mechanical engineering', 'me in mechanical engineering ', 'me mechanical engineering','me mech',
                'masters of engineering in  electrical and electronics engineering', 'master of engineering in  electrical and electronics engineering', 'me in  electrical and electronics engineering ', 'me  electrical and electronics engineering','me in eee','me eee',
                'masters of engineering in electronics & communication engineering', 'master of engineering in electronics & communication engineering', 'me in electronics & communication engineering ', 'me electronics & communication engineeringg', 'me in ece','me ece',
                "b.tech", "bachelor of technology", "Bachelor of Technology", "btech", "B.tech", "B.Tech","bachelors of technology", "b tech",'bachelor in computer application',
                "m.tech", "Master of Technology", "M.tech", "mtech", "M.Tech", "master of technology","masters of technology","m tech",
                "BCA", "bca", "B.C.A", " bachelor of computer application", "Bachelor of Computer Application",
                "BSC", "bsc", "B.sc", "bachelor of science", " Bachelor of Science", "BS","bfa","b.s","ddm (dual degree management) b. tech + mba",
                "MCA", "mca", "M.C.A", " master of computer application", "Master of Computer Application",
                "MSC", "msc", "M.sc", "master of science", "Master of Science", "Masters", "masters"
                "B.COM", "bachelor of commerce", "Bachelor of Commerce", "bcom","B.com","b.com",'b.a'
                "M.COM", "M.com", "master of commerce", "Master of Commerce", "mcom",
                "BBA", "bba", "bachelor of business administration", "Bachelor of Business Administration","bsc. in chemistry and biochemistry","bachelor of science in business administration",
                "MBA","master of business administration", "Master of Business Administration", 
                "BA", "Ba", "bachelor of arts", "Bachelor of Arts", "bachelor's", "Bachelors","bachelors in arts","bachelor in arts",
                "MA", "Ma", "master of arts", "Master of Arts",'Bachelors in Management','bachelors in management',
                "BE", "b.e","bachelor of engineering", "Bachelor of Engineering", "BE/B.tech",
                "ME", "master of engineering", "Master of Engineering","post graduate diploma",
                "MS", "master of science", " Master of Science", "Ms", "Master of Science (Intergrated)", "M.Tech Software Engineering (5 Year Integrated Programme)",
                "B.Arch", "b.arch", "bachelor of architecture", "Bachelor of Architecture",
                "PHD", "ph.d", "PH.D", "Doctor of Philosophy", "doctor of philosophy"}




certification_dict= {"microsoft certified azure ai fundamentals", "data science methodologies by ibm", "introduction to data science by microsoft",
                     "python beginner by microsoft", "google analytics by google", "the online marketing fundamentals by google",
                     "build your own chatbot- level 1 by ibm", "python for data science by ibm", "machine learning with python by ibm",
                     "streaming analytics basics for python developers by ibm", "365 Data science", "bosch automated mobility academy", 
                     "amazon online conference on machine learning and ai","intel ai academy", "voice design with amazon alexa by udemy",
                     "cisco certified networking engineer","365 data science", "udemy", "coursera", "great learning", "analytics vidhya", 
                     "linked in", "nptel", "guvi", "ibm", "aws", "gcp", "microsoft azure","microsoft certified professional developer",
                     "microsoft (mta)", "amazon web services (aws)", "oracle application express developer certification (oracle apex)", 
                     "cloudera certified developer for apache hadoop (ccdh)", "oracle certified professional(ocp) mysql 5.6 developer",
                     "oracle certified professional ocp (java se programmer, java me mobile application developer", "oracle certified associate (oca) java se programmer",
                     "ciw (web foundation associate, web design professional, web & mobile design professional, web development professional)", "red hat jboss certified developer",
                     "puppet labs certification program", "salesforce certified developer & advanced developer", "scrum alliance certified scrum developer (csd)"
                     "pmp agile certified practitioner (pmi-acp)", "harvard software engineering certificate"}   



app = Flask(__name__)

# Text preprocessing 
def cleaning(text):
    text = text.strip() # Stripping text
    text = re.sub('[^A-Za-z0-9.,\ ()-?><!$*_=+\{\}\/;`|₹\]\[\n%&"\']+', '', text) # remove the special characters 
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text) # remove the punctuation 
    text = re.sub('\n+','\n', text) # remove the next line characters
    text = re.sub(' +', ' ', text)  # remove the extra spaces
    text = re.sub('\w*\d\w*', '', text)
    text = text.replace('•', '', -1) # remove the bullet points
    text = re.sub(' +', ' ', text)
    return text

#Removing whitespaces
def remove(text):
    text = re.sub(' +', ' ', text)
    text = text.replace('\t', '', -1)
    text = text.replace('/', ' ', -1)
    return text

#stopwords removal
def stopwords_removal(text):
    stopwords = ['|', '-', '(', ')','A', 'having', 'for', 'Successfully', 'best', 'class',',','[]',
                 'to', 'i', 'my', 'myself','we','our', 'ours','ourselves','you','your','yours','yourself','m'
                 'yourselves','he','him','his','himself','she','her', 'hers','herself','its','itself','they',
                 'them','their','theirs','themselves','what','which','who','whom','this','that','these','those','am',
                 'is','are','was','were','been','being','have','has','had','having','do','does','did','doing','a',
                 'an','the','but','if','or','because','as','until','while','at','by','for','with','about',
                 'against','between','into','through','during','before', 'after','above','below','to','from','up','down',
                 'out','on','off','over','under','again','further','then','once','here','there','when','where','why',
                 'how','all','any','both','each','few','more','most','other','some','such','no','nor','not','only','own',
                 'same','so','than','too','very','can','will','just','don','should','now']
    querywords = text.split()
    resultwords  = [word for word in querywords if word.lower() not in stopwords]
    result = ' '.join(resultwords)
    return result    
 
# Extracting the skills from the text
def get_matches(s, keys, include_duplicates=False):
     pattern = re.compile('|'.join(map(re.escape, keys)))
     all_matches = pattern.findall(s, re.IGNORECASE)
     if not include_duplicates:
         all_matches = list(OrderedDict.fromkeys(all_matches).keys())
     else:
         return None
     return all_matches

#Function to extract Phone Numbers from string using regular expressions
def phone_numbers(path):
    regex1 = r'((?:\(?\+91\)?)?\d{10})'
    regex2 = r'\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}?\b'
    regexList = [regex1, regex2]
    for x in regexList:
        if re.findall(x, path):
            some_list = re.findall(x, path)     
            for y in some_list:
                found_regex_list = []
                found_regex_list.append(y)
                return found_regex_list     

# Extracting Emails
def extract_emails(path):
    reg_exp = re.compile(r'[a-zA-Z0-9\.\-+_]+@[a-zA-Z0-9\.\-+_]+\.[a-z]+')
    return re.findall(reg_exp, path)

# Extracting company Names
def company_names(path):
    reg = re.compile(r"\b[a-zA-Z]\w+(?:\.com?)?(?:[ -]+(?:&[ -]+)?[A-Z]\w+(?:\.com?)?){0,1}[,\s]+(?i:ltd|pvt|labs|consultancy services|technologies solutions|solution llp|fintech|Pvt.Ltd.|private limited|limited|software solutions|corporation limited|research and analytics|llc|inc|plc(?:rp)?|holding|gmbh)\b")    
    return re.findall(reg, path)  

# Captialize the output
def capitalize_nested(t):
    res=[]
    for s in t:
        if type(s) == list:
            res.append(capitalize_nested(s))
        else:
            res.append(s.capitalize())
    return res

# EXtracting urls
def URLsearch(stringinput):
    #regular expression
    regularex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|(([^\s()<>]+|(([^\s()<>]+)))))+(?:(([^\s()<>]+|(([^\s()<>]+))))|[^\s`!()[]{};:'\".,<>?«»“”‘’]))"
    #finding the url in passed string
    urlsrc = re.findall(regularex,stringinput)
    #return the found website url
    return [url[0] for url in urlsrc]

# Extracting Institute/University names
def edu(string):
    # findall() has been used 
    # with valid conditions for urls in string
    regex = re.compile(r"\b[a-zA-Z]\w+(?:\.com?)?(?:[ -]+(?:&[ -]+)?[A-Z]\w+(?:\.com?)?){0,2}[,\s]+(?i:university|institute to management|institute of technology|institute of engineering|business school|colleges of arts|university of|institute of management and research|school of(?:rp)?|science of technology)\b")
    return re.findall(regex,string)    

# Extracting Experience
def extract_experience(path):
    reg_exp =  "(\d+\.?\+?\d*?)\s+years?\s+.*?\s+experience" 
    return re.findall(reg_exp, path)

# Extracting Candidates Names
def extract_names(path):
    Tokens = []
    Sentences = nltk.sent_tokenize(path)
    for Sent in Sentences:
        Tokens.append(nltk.word_tokenize(Sent)) 
    Words_List = [nltk.pos_tag(Token) for Token in Tokens]
    Nouns_List = []
    for List in Words_List:
        for Word in List:
            if re.match('[NN.*]', Word[1]):
                 Nouns_List.append(Word[0])
    Names = []
    for Nouns in Nouns_List:
        if not wordnet.synsets(Nouns):
            Names.append(Nouns)
    return Names[:2]        


# cleaning education entities
def edu_cleaning (extracted_text):
  # Note: We are ignoring (#, ^) and other special chars
  # Stripping text
  extracted_text = extracted_text.strip()
  # handling web links starting with 'http'
  extracted_text = re.sub(r'http\S+', '', extracted_text)
  # handling web links ending with extensions like (.com), (.in) etc.
  extracted_text = re.sub(r'[\S]+\.(net|com|org|info|edu|gov|in|ai|uk|de|ca|jp|fr|au|us|ru|ch|it|nel|se|no|es|mil)[\S]*\s?','',extracted_text)
  # handling special characters
  extracted_text = re.sub('[^A-Za-z0-9.,\ :()-?><!$*_=+\{\}\/;`~@|₹\]\[\n%&"\']+', '', extracted_text)
  # handling extra next line chars
  extracted_text = re.sub('\n+','\n', extracted_text)
  # handling extra spaces
  extracted_text = re.sub('  +', ' ', extracted_text)
  # remove reference numbers
  extracted_text = re.sub(r'\[\d+\]', ' ', extracted_text)
  extracted_text = re.sub(' +', ' ', extracted_text)
  extracted_text =  re.sub("\n"," ",extracted_text)
  # handling bullet point
  extracted_text = extracted_text.replace('•', '', -1)
  #return extracted_text
  return extracted_text

# Function to convert  
def listToString(path): 
    str1 = "  " 
    return (str1.join(path))

@app.route("/output", methods=["GET","POST"])
def output():
    if request.method == "POST":
        text = request.form['text']
        text0 = remove(text)
        text1 = cleaning(text.lower())
        text2 = text.lower()
        text3 = edu_cleaning(text)
        text4 = text3.lower()
        company = company_names(text0)
        company = set(company)
        company =  [elem.upper() for elem in company ]
        company = listToString(company)
        Skills = get_matches(text1, skills)
        Skills = set(Skills)
        Skills = [elem.upper() for elem in Skills ]
        Skills = listToString(Skills)
        education = get_matches(text4,education_dict)
        education = set(education)
        education =  [elem.upper() for elem in education ]
        education = listToString(education)
        phone_number = phone_numbers(text)
        emails = extract_emails(text0)
        emails = listToString(emails)
        university = edu(text2)
        university = set(university)
        university = [elem.upper() for elem in university ]
        university = listToString(university)
        certifications = get_matches(text2,certification_dict)
        certifications = set(certifications)
        certifications =  [elem.upper() for elem in certifications]
        certifications = listToString(certifications)
        urls = URLsearch(text)
        urls = listToString(urls)
        experience = extract_experience(text3)
        experience  = listToString(experience)
        names = extract_names(text0)
        names =  listToString(names)
        result = {
            "Name":names,
            "Phone_Number":phone_number,
            "Email":emails,
            "Skills":Skills,
            "Education":education,
            "University":university,
            "Certifications":certifications,
            "Company":company,
            "Experience":experience,
            "URL":urls
        }
        return result
    else:
        return "Error"    

if __name__ == "__main__":
    app.run(debug=True)          