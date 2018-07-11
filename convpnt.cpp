#include <bitcoin/bitcoin.hpp>
using namespace bc;

int main(int argc, char** argv)
{
    ec_compressed key;
    decode_base16(key, argv[1]);
    ec_uncompressed kk;
    decompress(kk, key);
    data_chunk foo;
    for (int i = 1; i < 33; i++)
        foo.push_back(kk[i]);
    std::cout << "x = " << encode_base16(foo) << std::endl;
    foo.clear();
    for (int i = 33; i < kk.size(); i++)
        foo.push_back(kk[i]);
    std::cout << "y = " << encode_base16(foo) << std::endl;
    return 0;
}

