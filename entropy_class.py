from bitarray import bitarray


class entropy:

    def __init__(self):
        self.entropy = bitarray()
        self._collect_entropy()

    def _unbias(self, collection):
        return bitarray([collection[i] for i in range( 0 ,len(collection),2) if collection[i] != collection[i+1]])

    def collect(self):
        self._collect_entropy()

    def get_entropy(self):
        return self.entropy

    def get_bytes(self):
        return self.entropy.tobytes()

    def to_bin_list(self):
        result = []
        for i in self.entropy.tolist():
            if i:
                result.append(1)
            else:
                result.append(0)
        return result

    def write_bin_in_text_file(self, filename):
        with open(filename, 'w') as f:
            for val in self.entropy:
                if val:
                    f.write('1\n')
                else:
                    f.write('0\n')
