from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# loader = PyPDFLoader('dl-curriculum.pdf')=
# docs = loader.load()
# splitter = CharacterTextSplitter(
#     chunk_size=200,
#     chunk_overlap=0,
#     separator=''
# )
# result = splitter.split_documents(docs)
# print(result[1].page_content).

text = """
The Journey of Coffee: From Ethiopian Highlands to Global Obsession
Coffee's story begins in the highlands of Ethiopia, where legend tells of a goat herder named Kaldi who noticed his goats becoming unusually energetic after eating berries from a certain tree. Curious, he tried the berries himself and experienced a similar burst of energy. Word of this discovery eventually reached a local monastery, where monks began experimenting with the berries to help them stay awake during long hours of prayer.
From Ethiopia, coffee cultivation spread to the Arabian Peninsula, particularly Yemen, by the 15th century. Sufi monasteries there used coffee to maintain focus during nighttime devotions, and it wasn't long before the drink moved beyond religious circles into everyday life. The city of Mocha in Yemen became a major trading hub, lending its name to a coffee variety still recognized today. Coffeehouses, known as qahveh khaneh, began appearing across the Middle East, becoming centers of social activity, conversation, and even political discussion.
By the 17th century, coffee had made its way to Europe, arriving first in Venice through trade routes. Initially met with suspicion by some clergy who viewed it as a "Muslim drink," coffee eventually won over the public after receiving papal approval. Coffeehouses sprang up across major European cities, including London, Paris, and Vienna, becoming hubs of intellectual exchange. In England, these establishments were often called "penny universities," since for the price of a cup of coffee, patrons could engage in stimulating conversations with scholars, merchants, and writers.
The plant itself eventually made its way to the Americas through colonial expansion. The Dutch introduced coffee cultivation to Java, while the French brought it to the Caribbean. Legend has it that a single coffee seedling, smuggled aboard a French naval ship in the 18th century, became the ancestor of much of the coffee grown in Latin America today. Brazil, in particular, would go on to become the world's largest coffee producer, a title it still holds.
Today, coffee is one of the most widely consumed beverages on the planet, second only to water in some estimates. It fuels morning routines, powers workplaces, and serves as a social ritual across nearly every culture. The rise of specialty coffee and third-wave coffee culture has transformed how people think about the drink, emphasizing origin, roasting technique, and brewing methods much like wine connoisseurship.
From a curious goat herder in Ethiopia to a global industry worth billions of dollars, coffee's journey reflects the interconnectedness of trade, culture, and human curiosity across centuries.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=0,
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)
