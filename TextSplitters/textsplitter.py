from langchain.text_splitter import CharacterTextSplitter


text="""Virat Kohli (born 5 November 1988)[a] is an Indian international cricketer who plays ODI cricket for the national team and is a former captain in all formats.[3] He is a right-handed batsman and occasional right-arm medium pace bowler. Considered one of the greatest all-format batsmen in the history of cricket, he is called the King, the Chase Master, and the Run Machine for his skills, records and ability to lead his team to victory.[4] Kohli is the highest run-scorer in the Indian Premier League, third in T20I, third in ODI, and third in international cricket.[5] He has the most ODI centuries and second-most centuries in international cricket.[6] Kohli is also the most successful Test captain of India with back-to-back Test mace wins and most victories in his tenure.[7] He is the only batter to earn 900 rating points in all three formats.[8]

Kohli was the captain of the 2008 U19 World Cup winning team and was a crucial member of the teams that won 2011 ODI World Cup, 2013 Champions Trophy, 2024 T20 World Cup, and 2025 Champions Trophy. He plays for Royal Challengers Bengaluru in the Indian Premier League and for Delhi in domestic cricket. In 2013, Kohli was ranked number one in the ODI batting rankings. In 2015, he achieved the same in T20I.[9] In 2018, he was ranked number one in Test, making him the only Indian to hold the number one spot in all three formats. He is the first player to score 20,000 runs in a decade. He was the Cricketer of the Decade for 2011 to 2020.[10]

Kohli has won ten ICC Awards, making him the most awarded player in international cricket history. He won the ODI Player of the Year award four times in 2012, 2017, 2018, and 2023. He won the Cricketer of the Year award, on two occasions, in 2017 and 2018. In 2018, he became the first player to win all three major awards including Cricketer of the Year, ODI Player of the Year and Test Player of the Year in the same year. He was honored with the Spirit of Cricket Award in 2019 and given the Cricketer of the Decade and ODI Cricketer of the Decade in 2020. Kohli was named the Wisden Leading Cricketer in the World for three consecutive years.

Kohli has the most Player of the Series and second most Player of the Match awards to his name in all three formats combined. He was honoured with the Arjuna Award in 2013, the Padma Shri in 2017, and India's highest sporting honour, the Khel Ratna Award, in 2018. Time included him on its 100 most influential people in the world list in 2018.

After winning the 2024 T20 World Cup and winning the Player of the Match award in the final, Kohli announced his retirement from T20Is.[11] On 12 May 2025, aged 36, he announced his retirement from the Test format.[12] He is married to actress Anushka Sharma, and they have two children.[13]

Early life
Kohli was born on 5 November 1988 in Delhi into a Punjabi Hindu family. His mother Saroj Kohli is as a housewife while his father Prem Nath Kohli worked as a criminal lawyer. He has an elder brother Vikas and an elder sister Bhawna.[14] His formative years were spent in Uttam Nagar. His early education was at Vishal Bharti Public School.[15] As per his family, Kohli exhibited an early affinity for cricket as a 3-year-old. He would pick up a bat and request his father bowl to him.[16]

In 1998, the West Delhi Cricket Academy was created. In May, his father arranged for him to meet Rajkumar Sharma.[17] Upon the suggestion of their neighbours, Kohli's father considered enrolling his son in a professional cricket academy, as they believed his ability merited more than gully cricket.[18] He was unable to secure a place in the U-14 Delhi team, due to extraneous factors. His father reportedly received offers to relocate his son to influential clubs, which would ensure his selection, but he declined the proposals.

Kohli found his way into the U-15 team.[17] He received training at the academy and participated in matches at the Sumeet Dogra Academy located at Vasundhara Enclave.[19] In pursuit of furthering his cricketing career, he transferred to Saviour Convent School during his ninth-grade education.[18]

On 18 December 2006, his father died of a stroke.[15][18] As per his mother, Kohli's demeanour shifted noticeably after his father's death. He took on cricket with newfound seriousness, prioritising playing time and dedicating himself fully to the sport.[18] Kohli's family resided in Meera Bagh, Paschim Vihar until the year 2015, after which they relocated to Gurgaon.[20]"
splitter.split_text("This is a long text that needs to be split into smaller chunks for better processing and understanding. The text will be divided based on the specified chunk size and overlap, ensuring that each chunk is manageable and coherent.")
"""

splitter= CharacterTextSplitter(
    separator="",
    chunk_size=100,
    chunk_overlap=0
)

result=splitter.split_text(text)
print(result[0])