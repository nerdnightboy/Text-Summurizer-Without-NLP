import heapq

# Split text into words or sentences
def tokenize(text):
    sentences = text.split('.')
    print("Tokenized Sentences :" + str(sentences))
    print(" ")
    tokens = [sentence.split() for sentence in sentences]
    return tokens

# Remove common words
def removeStopwords(tokens):
    stopwords = ['the', 'is', 'and', 'to', 'in', 'a', 'of', 'for', 'on', 'with']
    filtered_tokens = []
    for sentence in tokens:
        filtered_tokens.append([word for word in sentence if word.lower() not in stopwords])
    return filtered_tokens

# Calculate word frequency
def calWordFreq(tokens):
    word_freq = {}
    for sentence in tokens:
        for word in sentence:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
    return word_freq

# Score sentences based on word frequency
def sentenceScore(sentences, word_freq):
    sentence_scores = {}
    for i, sentence in enumerate(sentences):
        score = 0
        for word in sentence:
            score += word_freq[word]
        sentence_scores[i] = score
    return sentence_scores

def summarize(text):
    sentences = tokenize(text)
    print("Tokenized words : " + str(sentences))
    print(" ")
    sentences = removeStopwords(sentences)
    print("After removing stopwords text : " + str(sentences))
    print(" ")
    word_freq = calWordFreq(sentences)
    print("word frequencies : " + str(word_freq))
    print(" ")
    sentence_scores = sentenceScore(sentences, word_freq)
    print("Sentence Score : " + str(sentence_scores))
    print(" ")
    
    # Select top sentences based on scores
    top_sentences = heapq.nlargest(10, sentence_scores, key=sentence_scores.get)
    
    # Generate summary
    summary = ". ".join(" ".join(sentences[i]) for i in sorted(top_sentences))
    return summary

input_text = """The Last Gift

She had always loved Christmas. The lights, the music, the presents. She especially loved the presents. She would spend hours browsing online, looking for the perfect gifts for her family and friends. She would wrap them with care, adding ribbons and bows and tags. She would place them under the tree, admiring how they looked. She would imagine the joy and surprise on the faces of her loved ones when they opened them.

But this year was different. This year, she had no one to give gifts to. Her parents had passed away in a car accident. Her brother had moved to another country and cut off contact. Her best friend had betrayed her and stolen her boyfriend. She felt alone and bitter. She hated Christmas. She hated the world.

She decided to buy herself a gift. Something expensive and extravagant. Something that would make her feel better. She ordered a diamond necklace online, using her credit card. She didn't care about the debt. She didn't care about anything.

The necklace arrived on Christmas Eve. She opened the package, expecting to feel a surge of happiness. But she felt nothing. The necklace was cold and hard and lifeless. It didn't sparkle. It didn't shine. It didn't make her smile.

She threw it on the floor, disgusted. She cried, feeling empty and hopeless. She wished she had someone to talk to. Someone to hug. Someone to love.

She heard a knock on the door. She ignored it, thinking it was a delivery person or a salesperson. She didn't want to see anyone. She didn't want to talk to anyone.

The knock persisted, louder and more urgent. She got up, annoyed. She opened the door, ready to slam it in the face of whoever was bothering her.

She saw a little girl, holding a small box wrapped in red paper. The girl had curly brown hair and bright green eyes. She wore a red dress and a white coat. She smiled, showing two missing front teeth.

"Hi, I'm Lily," the girl said. "I live next door. I made this for you. Merry Christmas!"

She handed her the box, then ran away, waving. She was gone before she could say anything.

She stared at the box, confused. She didn't know the girl. She didn't know why she gave her a gift. She didn't know what to do.

She brought the box inside, curious. She unwrapped it, carefully. She opened it, slowly.

Inside, there was a snow globe. A tiny replica of her house, surrounded by snow and trees and lights. A tiny figure of herself, standing by the door. A tiny figure of the girl, holding a box.

She shook the globe, gently. The snowflakes swirled and danced. The lights twinkled and glowed. The figures smiled and hugged.

She felt a warm sensation in her chest. A tear rolled down her cheek. She smiled, softly.

She realized that she had received the best gift of all. A gift of kindness. A gift of friendship. A gift of hope.

She put the globe on the table, next to the necklace. She picked up the necklace, admiring it. It sparkled. It shined. It made her smile.

She put it on, feeling beautiful. She grabbed her coat, feeling excited. She ran outside, feeling alive.

She wanted to thank the girl. She wanted to give her a hug. She wanted to be her friend.

She knocked on the door, eagerly. She waited, patiently.

The door opened, slowly.

"Merry Christmas!" she said. """

summary = summarize(input_text)
print(summary)
