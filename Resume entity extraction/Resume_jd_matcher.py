# -*- coding: utf-8 -*-
"""Copy of Set_Rules.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cvfcyq7so3TinXzvVo0tftGu2JU1zUry
"""

!pip install pdfminer.six
!pip install docx2txt==0.8

import docx2txt
from pdfminer.high_level import extract_text
import re
import string
import pandas as pd
from collections import OrderedDict

path_resume = '/content/RohitResume(1).docx'
path_jd = '/content/drive/MyDrive/JDs/Deep Learning Engineer.docx.pdf'

# Converting docx,pdf into Text
def get_text(file):
    File = file
    text = []
    if File[-5:] == '.docx':
        text = docx2txt.process(File)
    elif File[-4:] == '.pdf':
        text = extract_text(File)
    else:
        return "Sorry! the file format is not supported. The input supports only (DOCX, PDF) formats."
    return " ".join(text.split('\n'))  

skills_dict = {'microsoft word', 'data analysis', 'transformers', 'numpy', 'numpy', 'ms sql', 'natural language processing', 'tensorflow and keras',
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
          'team player leadership','relationship building','consumer engagement team management','social media campaign building','tensorflow', 'keras', 'pytorch', 'caffe', 'mxnet'}    

# Extracting the skills from the text
def get_matches(s, keys, include_duplicates=False):
     pattern = re.compile('|'.join(map(re.escape, keys)))
     all_matches = pattern.findall(s, re.IGNORECASE)
     if not include_duplicates:
         all_matches = list(OrderedDict.fromkeys(all_matches).keys())
     else:
         return None
     return all_matches

# Extracting Experience
def extract_experience_from_jd(path):
    regex1 = r"(\d+\.?\-\+?\d*?)\s+years" 
    regex2 = r"(\d+\.?\+?\d*?)\s+years?\s+.*?\s+experience"
    regexList = [regex1, regex2]
    for x in regexList:
        if re.findall(x, path):
            some_list = re.findall(x, path)     
            for y in some_list:
                found_regex_list = []
                found_regex_list.append(y)
                return found_regex_list   
#Cleaning_jd
def cleaning_jd(text):
    text = text.strip() # Stripping text
    text = re.sub('[^A-Za-z0-9.,\ ()-?><!$*_=+\{\}\/;`|₹\]\[\n%&"\']+', '', text) # remove the special characters 
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text) # remove the punctuation 
    text = re.sub('\n+','\n', text) # remove the next line characters
    text = re.sub(' +', ' ', text)  # remove the extra spaces
    text = re.sub('\w*\d\w*', '', text)
    text = text.replace('•', '', -1) # remove the bullet points
    text = re.sub(' +', ' ', text)
    return text


# cleaning education entities
def edu_cleaning_jd (extracted_text):
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
  return extracted_text




# Function to convert  
def listToString_jd(path): 
    str1 = "  ".join(path) 
    return str1

# list
my_list_jd = ["Minimum","minimum", "Atleast","atleast","Maximum","maximum","Overall","overall","having","Having","Good Knowledge", "good knowledge"]

# Extracting Experience
def extract_experience_resume(path):
    regex1 = r"(\d+\.?\-\+?\d*?)\s+years" 
    regex2 = r"(\d+\.?\+?\d*?)\s+years?\s+.*?\s+experience"
    regexList = [regex1, regex2]
    for x in regexList:
        if re.findall(x, path):
            some_list = re.findall(x, path)     
            for y in some_list:
                found_regex_list = []
                found_regex_list.append(y)
                return found_regex_list    

#Removing whitespaces
def remove_resume(text):
    text = re.sub(' +', ' ', text)
    text = text.replace('\t', '', -1)
    text = text.replace('/', ' ', -1)
    return text

#converting tuple      
def conv_resume(x):
  try:
    y = '{} - {}'.format(x[0][0], x[0][1])
    for i in range(1, len(x)):
        y += '\n{} - {}'.format(x[i][0], x[i][1])
    return y 
  except:
    return "An exception occurred"  


# Extracting the skills from the text
def month_year(s):
     months = r"january|Jan|January|jan|jan.|February|Feb|february|feb|feb.|Feb.|March|march|mar|Mar|mar.|Mar.|April|april|Apr|apr|apr.|Apr.|May|may|may.|May.|june|June|June |jun.|Jun.|jun|Jun|july|Jul|jul|July|July |july.|July.|august|August|August.|august.|Aug|aug|Aug.|aug.|september|September|sep|sept|Sep|Sept.|sept.|october|October||Oct|oct|oct.|Oct.|november|November|nov|Nov|nov|Nov.|december|December|dec|Dec|dec.|Dec."
     pattern = re.compile(fr"(?i)((?:{months}) *\d{{2,4}})  *(?:-|–|to)  *(Present|till now|Till Date|present|Till now|Till Now|Current|current|At present|at present|(?:{months}) *\d{{2,4}})")
     all_matches = pattern.findall(s, re.IGNORECASE)
     return list(all_matches)


#parsing date
def parse_date(x, fmts=("%b %Y", "%B %Y")):
    for fmt in fmts:
        try:
            return datetime.strptime(x, fmt)
        except ValueError:
            pass
def total_experience_companies(path):
  try:
    months = "|".join(calendar.month_abbr[1:] + calendar.month_name[1:])
    pattern = fr"(?i)((?:{months}) *\d{{2,4}}) *(?:-|–|to) *(present|(?:{months}) *\d{{2,4}})"
    total_experience = None
    for start, end in re.findall(pattern, path):
        if end.lower() == "present":
            today = datetime.today()
            end = f"{calendar.month_abbr[today.month]} {today.year}"
        duration = relativedelta(parse_date(end), parse_date(start))
        if total_experience:
            total_experience += duration
        else: 
            total_experience = duration
        print(f"{start}-{end} ({duration.years} years, {duration.months} months)")
    if total_experience:
        print(f"total experience:  {total_experience.years} years, {total_experience.months} months")
    else:
        print("couldn't parse text") 
  except:
    return "Format not accepted" 


# Text preprocessing 
def date_cleaning_resume(text):
  try:
    text = text.replace('.', '')
    text = text.replace('till now', 'present') 
    text = text.replace('Till now', 'present')
    text = text.replace('Present', 'present')
    text = text.replace('Current', 'present')
    text = text.replace('current', 'present')
    text = text.replace('At present', 'present')
    text = text.replace('Till Date', 'present')
    text = text.replace('till Date', 'present')
    text = re.sub('(\d+(\.\d+)?)', r' \1 ', text).strip()
    return text
  except:
    return "couldn't parse text"



#Remove ordinal data
def ordinal_resume(path):
    a_string = path
    remove_characters = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th", "14th", "15th", "16th", "17th", "18th","19th", "20th", "21st", "22nd", "23rd", "24th", "25th", "26th", "27th", "28th", "29th", "30th", "31st"]
    for character in remove_characters:
        a_string = a_string.replace(character, "")
    return a_string




#two digit converstion
def two_digit_resume(path):
  try:
    months = "|".join(calendar.month_abbr[1:] + calendar.month_name[1:])
    pattern = fr"(?i)((?:{months}) *\d{{2}}) *(?:-|–) *(present|(?:{months}) *\d{{2}})"
    pattern2 = fr"(?i)((?:{months}) *\d{{4}}) *(?:-|–) *(present|(?:{months}) *\d{{4}})"
    four_dig = re.findall(pattern2, path)
    four_dig = [tuple(x) for x in four_dig]
    h = []
    h.extend(four_dig)
    for start in re.findall(pattern, path):  
        start = list(start)
        str1 = ','.join(start)
        s1 = '20'.join(str1.split())
        s2 = re.sub(r'(?<=[.,]) (?=[^\s])', r' ',s1)
        str2 = list(s2.split(" "))
        str2 = [x for s in str2 for x in s.split()]
        str2 = [x for xs in str2 for x in xs.split(',')]
        str2 = tuple(str2)
        h.append(str2)
    return h
  except:
    return "Incorrect Format" 


# Text preprocessing 
def cleaning_resume(text):
    text = text.strip() # Stripping text
    text = re.sub('[^A-Za-z0-9.,\ ()-?><!$*_=+\{\}\/;`|₹\]\[\n%&"\']+', '', text) # remove the special characters 
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text) # remove the punctuation 
    text = re.sub('\n+','\n', text) # remove the next line characters
    text = re.sub(' +', ' ', text)  # remove the extra spaces
    text = re.sub('\w*\d\w*', '', text)
    text = text.replace('•', '', -1) # remove the bullet points
    text = re.sub(' +', ' ', text)
    return text



# cleaning education entities
def edu_cleaning_resume(extracted_text):
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
  return extracted_text



# Function to convert  
def listToString_resume(path): 
    str1 = "  ".join(path) 
    return str1

# Companies names
def company_names_resume(path):
    reg = re.compile(r"\b[a-zA-Z]\w+(?:\.com?)?(?:[ -]+(?:&[ -]+)?[A-Z]\w+(?:\.com?)?){0,1}[,\s]+(?i:ltd|pvt|labs|consultancy services|technologies solutions|solution llp|fintech|Pvt.Ltd.|private limited|limited|software solutions|corporation limited|research and analytics|llc|inc|plc(?:rp)?|holding|gmbh)\b")    
    return re.findall(reg, path) 


#Rules setting
def matching_score(row):
  if row['SKILLS_FROM_JD'] == row['SKILLS_FROM_RESUME'] and row['DECISION_WORDS_JD']== 'NaN':
      if row['WORK_EXPERIENCE_JD'] == row['WORK_EXPERIENCE_RESUME']:
          return 100  
  if row['SKILLS_FROM_JD'] == row['SKILLS_FROM_RESUME'] and row['DECISION_WORDS_JD']== 'NaN':
      if row['WORK_EXPERIENCE_JD'] > row['WORK_EXPERIENCE_RESUME']:
          return row['WORK_EXPERIENCE_RESUME']/row['WORK_EXPERIENCE_JD']*100
  if row['SKILLS_FROM_JD'] == row['SKILLS_FROM_RESUME'] and row['DECISION_WORDS_JD']== 'Atleast':
      if row['WORK_EXPERIENCE_JD'] > row['WORK_EXPERIENCE_RESUME']:
          return row['WORK_EXPERIENCE_RESUME']/row['WORK_EXPERIENCE_JD']*100 
  if row['SKILLS_FROM_JD'] == row['SKILLS_FROM_RESUME'] and row['DECISION_WORDS_JD']== 'Minimum':
      if row['WORK_EXPERIENCE_JD'] > row['WORK_EXPERIENCE_RESUME']:
          return row['WORK_EXPERIENCE_RESUME']/row['WORK_EXPERIENCE_JD']*100
  if row['SKILLS_FROM_JD'] == row['SKILLS_FROM_RESUME'] and row['DECISION_WORDS_JD']== 'Maximum':
      if row['WORK_EXPERIENCE_JD'] > row['WORK_EXPERIENCE_RESUME']:
          return row['WORK_EXPERIENCE_RESUME']/row['WORK_EXPERIENCE_JD']*100
  if row['SKILLS_FROM_JD'] == row['SKILLS_FROM_RESUME'] and row['DECISION_WORDS_JD']== 'Good Knowledge':
      if row['WORK_EXPERIENCE_JD'] > row['WORK_EXPERIENCE_RESUME']:
          return row['WORK_EXPERIENCE_RESUME']/row['WORK_EXPERIENCE_JD']*100 
  if row['SKILLS_FROM_JD'] == row['SKILLS_FROM_RESUME'] and row['DECISION_WORDS_JD']== 'having':
      if row['WORK_EXPERIENCE_JD'] > row['WORK_EXPERIENCE_RESUME']:
          return row['WORK_EXPERIENCE_RESUME']/row['WORK_EXPERIENCE_JD']*100 
  if row['SKILLS_FROM_JD'] == row['SKILLS_FROM_RESUME'] and row['DECISION_WORDS_JD']== 'NaN':
      if row['WORK_EXPERIENCE_JD'] < row['WORK_EXPERIENCE_RESUME']:
          return 100
  if row['SKILLS_FROM_JD'] == row['SKILLS_FROM_RESUME'] and row['DECISION_WORDS_JD']== 'Atleast':
      if row['WORK_EXPERIENCE_JD'] < row['WORK_EXPERIENCE_RESUME']:
          return row['WORK_EXPERIENCE_RESUME']/row['WORK_EXPERIENCE_JD']*100 
  if row['SKILLS_FROM_JD'] == row['SKILLS_FROM_RESUME'] and row['DECISION_WORDS_JD']== 'Minimum':
      if row['WORK_EXPERIENCE_JD'] < row['WORK_EXPERIENCE_RESUME']:
          return row['WORK_EXPERIENCE_RESUME']/row['WORK_EXPERIENCE_JD']*100
  if row['SKILLS_FROM_JD'] == row['SKILLS_FROM_RESUME'] and row['DECISION_WORDS_JD']== 'Maximum':
      if row['WORK_EXPERIENCE_JD'] < row['WORK_EXPERIENCE_RESUME']:
          return row['WORK_EXPERIENCE_RESUME']/row['WORK_EXPERIENCE_JD']*100
  if row['SKILLS_FROM_JD'] == row['SKILLS_FROM_RESUME'] and row['DECISION_WORDS_JD']== 'Good Knowledge':
      if row['WORK_EXPERIENCE_JD'] < row['WORK_EXPERIENCE_RESUME']:
          return row['WORK_EXPERIENCE_RESUME']/row['WORK_EXPERIENCE_JD']*100 
  if row['SKILLS_FROM_JD'] == row['SKILLS_FROM_RESUME'] and row['DECISION_WORDS_JD']== 'having':
      if row['WORK_EXPERIENCE_JD'] < row['WORK_EXPERIENCE_RESUME']:
          return row['WORK_EXPERIENCE_RESUME']/row['WORK_EXPERIENCE_JD']*100   
  if row['SKILLS_FROM_JD'] == row['SKILLS_FROM_RESUME'] and row['DECISION_WORDS_JD']== 'Atleast':
      if row['WORK_EXPERIENCE_JD'] == row['WORK_EXPERIENCE_RESUME']:
          return 100 
  if row['SKILLS_FROM_JD'] == row['SKILLS_FROM_RESUME'] and row['DECISION_WORDS_JD']== 'Minimum':
      if row['WORK_EXPERIENCE_JD'] == row['WORK_EXPERIENCE_RESUME']:
          return 100
  if row['SKILLS_FROM_JD'] == row['SKILLS_FROM_RESUME'] and row['DECISION_WORDS_JD']== 'Maximum':
      if row['WORK_EXPERIENCE_JD'] == row['WORK_EXPERIENCE_RESUME']:
          return 100
  if row['SKILLS_FROM_JD'] == row['SKILLS_FROM_RESUME'] and row['DECISION_WORDS_JD']== 'Good Knowledge':
      if row['WORK_EXPERIENCE_JD'] == row['WORK_EXPERIENCE_RESUME']:
          return 100 
  if row['SKILLS_FROM_JD'] == row['SKILLS_FROM_RESUME'] and row['DECISION_WORDS_JD']== 'having':
      if row['WORK_EXPERIENCE_JD'] == row['WORK_EXPERIENCE_RESUME']:
          return 100                                                             
  if row['SKILLS_FROM_JD'] != row['SKILLS_FROM_RESUME'] and row['DECISION_WORDS_JD']== 'NaN':
      return 0
  if row['SKILLS_FROM_JD'] == 'NaN' and row['DECISION_WORDS_JD']== 'NaN':
      return 100
  if row['SKILLS_FROM_RESUME'] == 'NaN' and row['WORK_EXPERIENCE_RESUME']== 'NaN':
      return 0         
          
#########################################################################################################################################################################

def main():
    text_res = get_text(path_resume)
    text0_res = remove_resume(text_res)
    text1_res = cleaning_resume(text_res.lower())
    text3_res = edu_cleaning_resume(text_res)
    exp_resume = extract_experience_resume(text3_res)
    exp_resume = exp_resume[0]
    exp_resume = exp_resume[0]
    skills_resume = get_matches(text1_res,skills_dict)
    #print(skills_resume)
    t = remove_resume(text_res)
    t = t.replace('(','')
    t = t.replace(')','')
    t = t.replace('-',' to ')
    t = ordinal_resume(t)
    t = month_year(t)
    t = conv_resume(t)
    t = date_cleaning_resume(t)
    t = two_digit_resume(t)
    t = conv_resume(t)
    t = date_cleaning_resume(t)
    total_exp_resume = exp_resume
    #print(total_exp_resume)
    dataframe_result_res= pd.DataFrame({'SKILLS_FROM_RESUME':  pd.Series(skills_resume), 'WORK_EXPERIENCE_RESUME': pd.Series(exp_resume)})
    #print(dataframe_result_res)
########################################################
    text_jd = get_text(path_jd)
    text1_jd = cleaning_jd(text_jd.lower())
    text3_jd = edu_cleaning_jd(text_jd)
    exp_jd = extract_experience_from_jd(text3_jd)
    exp_jd = exp_jd[0]
    exp_jd = exp_jd[0]
    skills_jd = get_matches(text1_jd,skills_dict)
    #print(skills_jd)
    decision_jd = get_matches(text3_jd,my_list_jd)
    dataframe_result_jd= pd.DataFrame({'SKILLS_FROM_JD':  pd.Series(skills_jd), 'DECISION_WORDS_JD':  pd.Series(decision_jd), 'WORK_EXPERIENCE_JD': pd.Series(exp_jd)})
    #print(dataframe_result_jd)
########################################################
    #dataframe_final = [dataframe_result_res,dataframe_result_jd]
    Final_data = pd.concat([dataframe_result_jd, dataframe_result_res], axis=1, ignore_index=False)
    #print(dataframe_final)
    Final_data[['WORK_EXPERIENCE_JD','WORK_EXPERIENCE_RESUME']] = Final_data[['WORK_EXPERIENCE_JD','WORK_EXPERIENCE_RESUME']].fillna(0)
    Final_data[['WORK_EXPERIENCE_JD','WORK_EXPERIENCE_RESUME']] = Final_data[['WORK_EXPERIENCE_JD','WORK_EXPERIENCE_RESUME']].astype(int)
    Final_data['DECISION_WORDS_JD'] = Final_data['DECISION_WORDS_JD'].fillna('NaN')
    Final_data['SKILLS_FROM_JD'] = Final_data['SKILLS_FROM_JD'].fillna('NaN')
    Final_data['SKILLS_FROM_RESUME'] = Final_data['SKILLS_FROM_RESUME'].fillna('NaN')
    Final_data['Matching_score'] = Final_data.apply(lambda row: matching_score(row), axis=1 )
    print(Final_data.head())
    Final_data.to_csv('jd___.csv')

if __name__ == "__main__":
     main()

def matching_score(row):
  #rule1: if Exp_skills_JD and Decision_words is given as Not mentioned in JD 
  if row['SKILLS_FROM_JD'] == 'NaN' and row['DECISION_WORDS_JD']== 'NaN':
    return '100%'
  #rule2: if Exp_skills_JD is mentioned is not mentioned but decision_word is giving in JD -- sub use case 1 Decision word== Atleast  
  if row['SKILLS_FROM_JD'] == 'NaN' and row['DECISION_WORDS_JD']== 'Atleast':
    return '100%' 
  #subusecase 2 Decision word= Minimum  
  if row['SKILLS_FROM_JD'] == 'NaN' and row['DECISION_WORDS_JD']== 'Minimum':
    return '100%'
  #sub use case 3 Decision word= Maximum  
  if row['SKILLS_FROM_JD'] == 'NaN' and row['DECISION_WORDS_JD']== 'Maximum':
    return '100%'   
  #sub use case 4 Decision word = Good Knowledege  
  if row['SKILLS_FROM_JD'] == 'NaN' and row['DECISION_WORDS_JD']== 'Good Knowledge':
    return '100%'
  #sub use case 5 Decision word= Having 
  if row['SKILLS_FROM_JD'] == 'NaN' and row['DECISION_WORDS_JD']== 'having':
    return '100%'     
  # corner case if Decision word is missing but exp is mentioned in JD: subcase1: if JD skill experience is greater than candidate exp in skills 
  if row['WORK_EXPERIENCE_JD'] > row['WORK_EXPERIENCE_RESUME'] and row['DECISION_WORDS_JD']=='NaN':
    return '75%'  
  #subcase2: if JD skill experience is equal candidate exp in skills  
  if row['WORK_EXPERIENCE_JD'] == row['WORK_EXPERIENCE_RESUME'] and row['DECISION_WORDS_JD']=='NaN': 
    return '100%' 
  #subcase2: if JD skill experience is less than candidate exp in skills  
  if row['WORK_EXPERIENCE_JD'] < row['WORK_EXPERIENCE_RESUME'] and row['DECISION_WORDS_JD']=='NaN':
    return '100%'
  #Jd_experience greater than thw work experience and work experience greater than the zero
  if row['WORK_EXPERIENCE_JD'] > row['WORK_EXPERIENCE_RESUME'] > 0 and row['DECISION_WORDS_JD']== 'NaN':
    return '50%' 
  #Rule3: If Exp_skills from JD is available and Decision Words are also there in that case
  #sub case1 Decision word== Atleast and jd skill exp is not equal to overall exp skills   2 years = 4 years   
  if row['DECISION_WORDS_JD']=='Atleast' and row['WORK_EXPERIENCE_JD'] > row['WORK_EXPERIENCE_RESUME']:
    return '75%'  
  if row['DECISION_WORDS_JD']=='Atleast' and row['WORK_EXPERIENCE_JD'] < row['WORK_EXPERIENCE_RESUME']:
    return '100%'
  #subcase1 Decision word== Atleast and jd skill exp is  equal to overall exp skills  
  if row['DECISION_WORDS_JD']=='Atleast' and row['WORK_EXPERIENCE_JD'] == row['WORK_EXPERIENCE_RESUME']:
    return '100%'
  #subcase2 Decision word== Minimum  
  if row['DECISION_WORDS_JD']=='Minimum' and row['WORK_EXPERIENCE_JD'] > row['WORK_EXPERIENCE_RESUME']:
    return '75%'  
  if row['DECISION_WORDS_JD']=='Minimum' and row['WORK_EXPERIENCE_JD'] < row['WORK_EXPERIENCE_RESUME']: 
    return '100%' 
  if row['DECISION_WORDS_JD']=='Minimum' and row['WORK_EXPERIENCE_JD'] == row['WORK_EXPERIENCE_RESUME']:
    return '100%'
  #subcase3 Decision word== Maximum      
  if row['DECISION_WORDS_JD']=='Maximum' and row['WORK_EXPERIENCE_JD'] > row['WORK_EXPERIENCE_RESUME']:
    return '100%'  
  if row['DECISION_WORDS_JD']=='Maximum' and row['WORK_EXPERIENCE_JD'] < row['WORK_EXPERIENCE_RESUME']: 
    return '75%' 
  if row['DECISION_WORDS_JD']=='Maximum' and row['WORK_EXPERIENCE_JD'] == row['WORK_EXPERIENCE_RESUME']:
    return '100%'
  #subcase4 Decision word==Good Knowledge   
  if row['DECISION_WORDS_JD']=='Good Knowledge' and row['WORK_EXPERIENCE_JD'] > row['WORK_EXPERIENCE_RESUME']:
    return '100%'  
  if row['DECISION_WORDS_JD']=='Good Knowledge' and row['WORK_EXPERIENCE_JD'] < row['WORK_EXPERIENCE_RESUME']: 
    return '100%' 
  if row['DECISION_WORDS_JD']=='Good Knowledge' and row['WORK_EXPERIENCE_JD'] == row['WORK_EXPERIENCE_RESUME']:
    return '100%'  
  #subcase4 Decision word==having        
  if row['DECISION_WORDS_JD']=='having' and row['WORK_EXPERIENCE_JD'] > row['WORK_EXPERIENCE_RESUME']:
    return '100%'  
  if row['DECISION_WORDS_JD']=='having' and row['WORK_EXPERIENCE_JD'] < row['WORK_EXPERIENCE_RESUME']: 
    return '100%' 
  if row['DECISION_WORDS_JD']=='having' and row['WORK_EXPERIENCE_JD'] == row['WORK_EXPERIENCE_RESUME']:
    return '100%'  
  return '0%'

dataset = Final_data.copy()

dataset.head()

dataset['Matching_score'] = dataset.apply(lambda row: matching_score(row), axis=1 )

dataset.head()
dataset.to_csv('mereged.csv')

dataset.dtypes

v = pd.read_csv('/content/jd_resume4 (2).csv')
v.head()

def cc(row):
  if row['WORK_EXPERIENCE_JD'] > row['WORK_EXPERIENCE_RESUME'] > 0 and row['DECISION_WORDS_JD']== 0:
    return '60%'

v['Matching_score'] = v.apply(lambda row: cc(row), axis=1)

v.head()

v = v.fillna(0)

def cc(row):
  if row['WORK_EXPERIENCE_JD'] > row['WORK_EXPERIENCE_RESUME'] > 0 and row['DECISION_WORDS_JD']== 'Atleast':
      return row['WORK_EXPERIENCE_RESUME']/row['WORK_EXPERIENCE_JD']*100


