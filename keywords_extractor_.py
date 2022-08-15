from keybert import KeyBERT

doc = """Main fabric 100% Polyamide Yoke 100% Polyester Coating 100% Polyurethane"""

kw_model = KeyBERT()
keywords = kw_model.extract_keywords(doc, keyphrase_ngram_range=(3, 3), stop_words='english',
                              use_maxsum=True, nr_candidates=30, top_n=3)

keywords1 = kw_model.extract_keywords(doc, keyphrase_ngram_range=(2, 2), stop_words='english',
                              use_mmr=True, diversity=0.2)
keywords2 = kw_model.extract_keywords(doc, keyphrase_ngram_range=(1, 1), stop_words=None)

print(keywords,
      keywords1,
      keywords2, sep= '\n')