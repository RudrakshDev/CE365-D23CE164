class RecursiveDescentParser:
    def __init__(self, input_str):
        self.input_str = input_str.replace(" ", "")  # Remove spaces
        self.index = 0
    
    def parse_S(self):
        if self.index < len(self.input_str) and self.input_str[self.index] == 'a':
            self.index += 1  # Match 'a'
            return True
        elif self.index < len(self.input_str) and self.input_str[self.index] == '(':
            self.index += 1  # Match '('
            if self.parse_L():
                if self.index < len(self.input_str) and self.input_str[self.index] == ')':
                    self.index += 1  # Match ')'
                    return True
            return False
        return False
    
    def parse_L(self):
        if self.parse_S():
            return self.parse_L_dash()
        return False
    
    def parse_L_dash(self):
        if self.index < len(self.input_str) and self.input_str[self.index] == ',':
            self.index += 1  # Match ','
            if self.parse_S():
                return self.parse_L_dash()
            return False
        return True  # Epsilon case (ϵ)
    
    def validate(self):
        if self.parse_S() and self.index == len(self.input_str):
            return "Valid string"
        else:
            return "Invalid string"

# Test cases
if __name__ == "__main__":
    inputs = ["(a)", "a", "(a,a)", "(a,(a,a),a)", "(a,a),(a,a)", "a)", "(a a,a", "a a, (a,a),a"]
    for inp in inputs:
        parser = RecursiveDescentParser(inp)
        print(f"Input: {inp} -> {parser.validate()}")
