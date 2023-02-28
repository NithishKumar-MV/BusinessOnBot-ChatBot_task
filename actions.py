class ActionAddition(Action):
    def name(self) -> Text:
        return "action_addition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        first_operand = float(tracker.get_slot("number"))
        second_operand = float(tracker.get_slot("number2"))

        result = first_operand + second_operand

