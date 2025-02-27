import _2_retrival as retrival
import _3_augment as augment
import _4_generate_response as generate


def get_answer(user_query):
    # Retrival of relevant data from the database
    profile_category = retrival.get_query_category(user_query)

    if "None" in profile_category:
        response = ("Sorry, I cannot answer this. "
                    "Please ask me if you have any queries about my professional experience.")
        print("\n",response)
        return response

    context = retrival.get_relevant_doc(profile_category)

    # Augment the data
    prompt = augment.get_prompt()

    # Generate response
    response = generate.generate_response(context, user_query, prompt)

    print("\n",response)

    return response
