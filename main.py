import _2_retrival as retrival
import _3_augment as augment
import _4_generate_response as generate
import streamlit
from streamlit import logger


def get_answer(user_query, app_logger: logger):

    app_logger.info("before get_query_category")

    # Retrival of relevant data from the database
    profile_category = retrival.get_query_category(user_query)

    app_logger.info(f"profile category : {profile_category}")

    if "None" in profile_category:
        app_logger.info("Category is None")

        response = ("Sorry, I cannot answer this. "
                    "Please ask me if you have any queries about my professional experience.")
        print("\n",response)
        return response

    app_logger.info("Before get relevant doc")

    context = retrival.get_relevant_doc(profile_category)

    app_logger.info("before get prompt")

    # Augment the data
    prompt = augment.get_prompt()

    app_logger.info("before generate response")

    # Generate response
    response = generate.generate_response(context, user_query, prompt)

    print("\n",response)

    return response
