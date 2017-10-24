        self.aozora = self.get_aozora()
        self.bigrams = self.get_bigrams()
        self.blogs = self.get_blogs()
        self.components = self.get_components()
        self.edict_common = self.get_edict_common()
        self.sentences = self.get_sentences()
        self.gsf = self.get_gsf()
        self.heisig = self.get_heisig()
        self.henshall = self.get_henshall()
        self.jinmeiyo = self.get_jinmeiyo()
        self.joyo = self.get_joyo()
        self.kanjidic = self.get_kanjidic()
        self.kklc = self.get_kklc()
        #self.kunyomi = self.get_kunyomi()
        self.kyoiku = self.get_kyoiku()
        self.mainichi = self.get_mainichi()
        self.meaning = self.get_meaning()
        self.novels = self.get_novels()
        #self.onyomi = self.get_onyomi()
        self.pattern = self.get_pattern()
        self.radicals = self.get_radicals()
        self.related_kanji = self.get_related_kanji()
        self.rm = self.get_rm()
        self.rtktwo = self.get_rtktwo()
        self.stroke_count = self.get_stroke_count()
        self.tags = []
        self.twitter = self.get_twitter()
        self.variety = self.get_variety()
        self.wikipedia = self.get_wikipedia()
        self.yatskov_novels = self.get_yatskov_novels()
        self.attributes = self.get_attribute_dict()
        self.rm2323 = get_rm2323_kanji()
        self.coll = get_coll()
        self.get_data()


    @lru_cache(maxsize=10)
    def get_data(self):
        kdic2 = read_json("Japanese/kanji/archive/kanjidic2.json")
        for i in range(len(kdic2)):
            row = kdic2[i]
            if row["literal"] == self.char:
                entry = {"char": self.char}
                entry = add_readings(row, entry)
                entry = add_meanings(row, entry)
                entry = get_freq_tags(row, entry)
                entry = get_jlpt_tags(row, entry)
                entry = get_grade_tags(row, entry)
                entry = get_strokecount_tags(row, entry)
                entry = get_heisig_tags(row, entry)
                entry = get_kic_tags(row, entry)
                entry = get_kklc_tags(row, entry)
                entry = get_rmfreq_tags(row, entry)

                try:
                    self.tags = [l for l in entry["tags"]]
                except:
                    pass
                try:
                    self.onyomi = [o for o in entry["readings"]["onyomi"]]
                except:
                    pass
                try:
                    self.kunyomi = [k for k in entry["readings"]["kunyomi"]]
                except:
                    pass
                try:
                    self.tags = [t for t in entry["tags"]]
                except:
                    pass
                try:
                    self.meanings = [m for m in entry["meanings"]]
                except:
                    pass

def parse_kanjidic2(kdic2=get_list_from_json_file(), kanji_list=[], kanji_dict={}):
    rm2323_kanji = get_rm2323_kanji()
    for i in range(len(kdic2)):
        row = kdic2[i]
        char = row["literal"]
        if char not in rm2323_kanji:
            continue
        else:
            entry = {"char": char}

            # char field
            kanji_dict[char] = {}
            kanji_dict[char]["char"] = char

    assert isinstance(kanji_dict, dict)
    return kanji_dict


    @lru_cache(maxsize=10)
    def get_twitter(self):
        with open("Japanese/kanji/data/frequency/twitter_kanji_frequency.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    @lru_cache(maxsize=10)
    def get_variety(self):
        with open("Japanese/kanji/data/frequency/kanji_freq_variety_sources.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    @lru_cache(maxsize=10)
    def get_wikipedia(self):
        with open("Japanese/kanji/data/frequency/yatskov_wikipedia_kanji.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break



    @lru_cache(maxsize=10)
    def get_yatskov_novels(self):
        with open("Japanese/kanji/data/frequency/yatskov_novels_kanji.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break




    @lru_cache(maxsize=10)
    def get_kyoiku(self):
        with open("Japanese/kanji/data/traditional/kyoiku_kanji.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    @lru_cache(maxsize=10)
    def get_mainichi(self):
        with open("Japanese/kanji/data/frequency/mainichi_kanji_by_wordfreq.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    @lru_cache(maxsize=10)
    def get_meaning(self):
        try:
            meaning = db.kanji.find({"name": self.char}, {"meaning": 1, "_id": 0})
            self.meaning  = meaning
            return(str(meaning))
        except:
            return []


    @lru_cache(maxsize=10)
    def get_news(self):
        with open("Japanese/kanji/data/frequency/kanji_freq_news.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    @lru_cache(maxsize=10)
    def get_novels(self):
        with open("Japanese/kanji/data/frequency/kanji_freq_novels.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    @lru_cache(maxsize=10)
    def get_pattern(self):
        with open('Japanese/kanji/data/mappings/patterns_by_kanji.csv') as infile:
            patterns_by_kanji = (l.strip().split('\t') for l in infile.readlines())
            for i in range(len(list(patterns_by_kanji)) - 1):
                try:
                    aline = next(patterns_by_kanji)
                    line = aline.split('\t')
                    kanji = line[0]
                    if kanji == self.char:
                        if len(line) > 1:
                            return line[1]
                        else:
                            return []
                        break
                except:
                    return []


    @lru_cache(maxsize=10)
    def get_radicals(self):
        rm2323 = get_rm2323_kanji()
        with open('Japanese/kanji/data/mappings/radicals_by_kanji.csv') as infile:
            radicals_by_kanji = (l.strip().split('\t') for l in infile.readlines())
            for i in range(len(list(radicals_by_kanji)) - 1):
                try:
                    aline = next(radicals_by_kanji)
                    line = aline.split('\t')
                    kanji = line[0]
                    if kanji == self.char:
                        if len(line) > 1:
                            return list({l for l in line[1].strip() if l in rm2323})
                        else:
                            return []
                        break
                except:
                    return []


    @lru_cache(maxsize=10)
    def get_related_kanji(self):
        rm2323 = get_rm2323_kanji()
        with open("Japanese/kanji/data/mappings/related_kanji.csv", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            for line in thelist:
                line = line.split('\t')
                if line[0] == self.char:
                    if len(line) > 1:
                        return list({l for l in line[1].strip() if l in rm2323})
                    else:
                        return []
                    break


    @lru_cache(maxsize=10)
    def get_rm(self):
        with open("Japanese/kanji/data/mixed/rm_kanji_rank_grouped.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    @lru_cache(maxsize=10)
    def get_rtktwo(self):
        with open("Japanese/kanji/data/pedagogical/rtk_2_example_order.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break

    @lru_cache(maxsize=10)
    def get_attribute_dict(self):
        return str([str(str(attr) + ': ' + str(value)) for attr, value in vars(self).items()])




    @lru_cache(maxsize=10)
    def get_aozora(self):
        with open("Japanese/kanji/data/frequency/aozora_kanji_freq.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    @lru_cache(maxsize=10)
    def get_bigrams(self):
        rm2323 = get_rm2323_kanji()
        with open("Japanese/kanji/data/mappings/kanji_bigrams.csv", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            for line in thelist:
                line = line.split('\t')
                if line[0] == self.char:
                    if len(line) > 1:
                        return list({l for l in line[1].strip() if l in rm2323})
                    else:
                        return []
                    break


    @lru_cache(maxsize=10)
    def get_blogs(self):
        with open("Japanese/kanji/data/frequency/blog_kanji_by_wordfreq.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break

    @lru_cache(maxsize=10)
    def get_components(self):
        rm2323 = get_rm2323_kanji()
        with open('Japanese/kanji/data/mappings/components_by_kanji.csv') as infile:
            components_by_kanji = (l.strip().split('\t') for l in infile.readlines())
            for i in range(len(list(components_by_kanji)) - 1):
                try:
                    aline = next(components_by_kanji)
                    line = aline.split('\t')
                    kanji = line[0]
                    if kanji == self.char:
                        if len(line) > 1:
                            return list({l for l in line[1].strip() if l in rm2323})
                        else:
                            return []
                        break
                except:
                    return []


    @lru_cache(maxsize=10)
    def get_components(self):
        rm2323 = get_rm2323_kanji()
        with open('Japanese/kanji/data/mappings/components_by_kanji.csv') as infile:
            components_by_kanji = (l.strip().split('\t') for l in infile.readlines())
            for i in range(len(list(components_by_kanji)) - 1):
                try:
                    aline = next(components_by_kanji)
                    line = aline.split('\t')
                    kanji = line[0]
                    if kanji == self.char:
                        if len(line) > 1:
                            return list({l for l in line[1].strip() if l in rm2323})
                        else:
                            return []
                        break
                except:
                        return []


    @lru_cache(maxsize=10)
    def get_heisig(self):
        with open("Japanese/kanji/data/pedagogical/heisig_kanji.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    @lru_cache(maxsize=10)
    def get_gsf(self):
        with open("Japanese/kanji/data/mixed/con_kolivas_gsf_list.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    @lru_cache(maxsize=10)
    def get_edict_common(self):
        with open("Japanese/kanji/data/frequency/kanji_in_edict_common_unsorted.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                return True



    @lru_cache(maxsize=10)
    def get_henshall(self):
        with open("Japanese/kanji/data/pedagogical/henshall_kanji.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    @lru_cache(maxsize=10)
    def get_jinmeiyo(self):
        with open("Japanese/kanji/data/traditional/jinmeiyo_kanji.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num + 2137 # Accounting for the kyoiku and joyo kanji
                        break


    @lru_cache(maxsize=10)
    def get_jlpt(self):
        with open("Japanese/kanji/data/traditional/jlpt_kanji.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    @lru_cache(maxsize=10)
    def get_joyo(self):
        with open("Japanese/kanji/data/traditional/joyo_non_kyoiku_kanji.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num + 1006 # Accounting for the kyoiku kanji
                        break


    @lru_cache(maxsize=10)
    def get_kanjidic(self):
        with open("Japanese/kanji/data/frequency/kanjidic_freq.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    @lru_cache(maxsize=10)
    def get_kic(self):
        with open("Japanese/kanji/data/pedagogical/kanji_in_context_kanji.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break



    @lru_cache(maxsize=10)
    def get_kklc(self):
        with open("Japanese/kanji/data/pedagogical/kklc_kanji.txt", mode="r", encoding="utf-8") as infile:
            thelist = [l.strip() for l in infile.readlines()]
            if self.char in set(thelist):
                for i, v in enumerate(thelist):
                    list_char = v.strip()
                    if self.char == v.strip():
                        char_num = i + 1
                        return char_num
                        break


    @staticmethod
    def write_csv(kanji_list=get_rm2323_kanji):
        with open('output/usefulkanji.csv', mode='w') as outfile:
            for char in kanji_list:
                line = str('\t'.join([char, char.mean, 
                    ''.join(char.related_kanji),
                 ''.join(char.onyomi),
                 ''.join(char.kunyomi),
                 ''.join(char.radicals),
                 ''.join(char.components),
                 ''.join(char.meanings),
                 char.pattern,
                 char.heisig,
                 char.kklc,
                 '\n']))
                outfile.writelines(line)
        return("Wrote CSV file to output/usefulkanji.csv")



    @staticmethod
    def get_csvs():
        kanji_csv_dict = {}
        for i in range(len(KANJI_CSVS)):
            with open(KANJI_CSVS[i]['csv_path'], mode='r', encoding='utf-8') as infile:
                kanji_csv_dict[KANJI_CSVS[i]['csv_name']]= [l.strip().split('\t').split(',') for l in infile.readlines()]
        return kanji_csv_dict


    @staticmethod
    def get_sets():
        kanji_set_dict = {}
        for i in range(len(UNORDERED_KANJI_LISTS)):
            with open(UNORDERED_KANJI_LISTS[i]['set_path'], mode='r', encoding='utf-8') as infile:
                kanji_set_dict[UNORDERED_KANJI_LISTS[i]['set_name']] = enumerate([l.strip() for l in infile.readlines()])
        return kanji_set_dict

    @classmethod
    def update_kanji_list_data_in_db():
        data = get_kanji_data()
        rmlist = update_db_whether_in_collection(data, data['rm2323'], filter_key='literal', var_name='rm2323')
        return "Updated kanji list"

        except:
            try:
                tofix = kdict[kanji]['top25000words'][0]['top25000words']
                for i in range(len(tofix)):
                    try:
                        avg = db.words.find_one({'word': tofix[i]}, {'_id': 0, 'average': 1})['average']
                        kdict[kanji]['top25000words'][0]['top25000words'][i] = (tofix[i], avg)
                    except:
                        continue
                allwords = wordset | sorted([z for z in kdict[kanji]['top25000words'][0]['top25000words']], key=lambda x: x[1])
            except:
                continue
