# from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline


# llm=HuggingFacePipeline(
#     model_id="HuggingFaceH4/zephyr-7b-beta",
#     task="text-generation", 
#     pipeline_kwargs=dict(
#         temperature=0.5,
#         max_new_tokens=100
#     )
# )


# model=ChatHuggingFace(llm=llm)

# result=model.invoke("what is the capital of India?")
# print(result.content)

# it will download the model from huggingface and run it locally.