def create_sorting_dict():
    glass_emojis = ["🪞", "🔮", "🥃", "🍸", "🍷", "🍺", "🍶", "🧴", "🧪", "🔬","🔭", "💉", "🏺"]
    plastic_emojis = ["💳", "🪪", "🧴", "🔫", "🪀", "🪁", "🧩", "🎮", "🕹️", "💾", "💿", "📀", "🖨️", "🛢️", "🗑️", "🪣", "🧺", "🛍️", "📏"]
    paper_emojis = ["📄", "📃", "📜", "📑", "🧻", "📰", "📒", "📔", "📕", "📖", "📗", "📘", "📙", "📚", "📓", "🗞️","🎫", "🧾", "📇", "📋", "📁", "📂", "🗂️", "💌", "📨", "📩", "✉️", "📦", "🏷️", "🪪"]
    metal_emojis = ["🔑", "🗝️", "⚙️", "⛓️", "🔗", "🛠️", "🔨", "🪚", "🪛", "🔧", "💣", "🪙", "💰", "💎", "🥇", "🥈", "🥉", "🏆", "🎖️", "✂️", "🔪", "🗡️", "🪓", "🪄", "🪝", "🪜", "🪠", "🛡️", "🪞", "🕰️", "⏰", "🚲", "🏍️", "🚗", "✈️", "🚀", "🚂", "🚇", "🛞", "⚔️", "🪺"]
    
    sorting_dict = {}
    for item in glass_emojis:
        sorting_dict[item] = "Стекло"
    for item in plastic_emojis:
        sorting_dict[item] = "Пластик"
    for item in paper_emojis:
        sorting_dict[item] = "Бумага"
    for item in metal_emojis:
        sorting_dict[item] = "Металл"
    
    return sorting_dict

def sortprob(item):
    sorting_dict = create_sorting_dict()
    return sorting_dict.get(item, "Я не могу распознать это")
