import xml.etree.ElementTree as ET

def parse_topics(topics_xml_s):
  root = ET.fromstring(topics_xml_s)
  return [{key: topic.findtext(key) for key in ['disease', 'gene', 'demographic']}
          for topic in root.findall('topic')]

def to_trec_topic(topic, topic_num, topic_to_title):
  trec_topic = '<TOP>\n'
  trec_topic += '<NUM>{}</NUM>\n'.format(topic_num)
  trec_topic += '<TITLE>{}</TITLE>\n'.format(topic_to_title(topic))
  trec_topic += '</TOP>\n'
  return trec_topic

def get_disease_and_gene_flat(topic): return '{} {}'.format(topic['disease'], topic['gene'])

def main():
  topics_path = './data/topics2018.xml'
  trec_topics_path = './etc/trec.topics.list'
  with open(topics_path) as fh:
    topics = parse_topics(fh.read())
  trec_topics = [to_trec_topic(topic, topic_num, get_disease_and_gene_flat)
                 for topic_num, topic in enumerate(topics, 1)]
  with open(trec_topics_path, 'w') as fh:
    fh.write('\n'.join(trec_topics))

if __name__ == "__main__": main()
