from summarizer import Summarizer
from transformers import AlbertTokenizer, AlbertModel

text = '''
John Christopher Depp II (born June 9, 1963) is an American actor, producer, and musician. He has been nominated for ten Golden Globe Awards, winning one for Best Actor for his performance of the title role in Sweeney Todd: The Demon Barber of Fleet Street (2007), and has been nominated for three Academy Awards for Best Actor, among other accolades. He is regarded as one of the world's biggest film stars.[1][2] Depp made his film debut in the 1984 film A Nightmare on Elm Street, before rising to prominence as a teen idol on the television series 21 Jump Street (1987–1990). He had a supporting role in Oliver Stone's 1986 war film Platoon and played the title character in the 1990 romantic fantasy Edward Scissorhands.
Depp has gained critical praise for his portrayals of inept screenwriter-director Ed Wood in the film of the same name (1994), undercover FBI agent Joseph D. Pistone in Donnie Brasco (1997), author J. M. Barrie in Finding Neverland (2004) and Boston gangster Whitey Bulger in Black Mass (2015). He has starred in a number of successful films, including Cry-Baby (1990), Dead Man (1995), Sleepy Hollow (1999), Charlie and the Chocolate Factory (2005), Corpse Bride (2005), Public Enemies (2009), Alice in Wonderland (2010) and its 2016 sequel, The Tourist (2010), Rango (2011), Dark Shadows (2012), Into the Woods (2014), and Fantastic Beasts: The Crimes of Grindelwald (2018). Depp also plays Jack Sparrow in the swashbuckler film series Pirates of the Caribbean (2003–present).
Depp is the tenth highest-grossing actor worldwide, as films featuring Depp have grossed over US$3.7 billion at the United States box office and over US$10 billion worldwide.[3] He has been listed in the 2012 Guinness World Records as the world's highest-paid actor, with earnings of US$75 million.[4][5] Depp has collaborated on eight films with director, producer, and friend Tim Burton. He was inducted as a Disney Legend in 2015.[6] In addition to acting, Depp has also worked as a musician. He has performed in numerous musical groups, including forming the rock supergroup Hollywood Vampires along with Alice Cooper and Joe Perry.
'''

albert_model = AlbertModel.from_pretrained('albert_xxlarge', output_hidden_states=True)
albert_tokenizer = AlbertTokenizer.from_pretrained('albert_xxlarge')
albert_model = Summarizer(custom_model=albert_model, custom_tokenizer=albert_tokenizer, random_state = 7)
output = albert_model(text, min_length=10, ratio=0.01)
print(output)

# transformers\src\transformers\models\albert\convert_albert_original_tf_checkpoint_to_pytorch.py
# --tf_checkpoint_path albert_xxlarge/model.ckpt-best
# --albert_config_file albert_xxlarge/albert_config.json
# --pytorch_dump_path albert_xxlarge/pytorch_model.bin