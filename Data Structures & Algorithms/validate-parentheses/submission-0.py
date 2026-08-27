class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        valid = {'}':'{',')':'(',']':'['}

        for c in s:
            if c in valid:
                if st and st[-1] == valid[c]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c)
        return True if not st else False

        