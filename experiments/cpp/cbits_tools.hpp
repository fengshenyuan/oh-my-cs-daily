unsigned int reverse_bits(unsigned int value)
{
	unsigned int reture_value	 = 0;
	unsigned int uint_bit_sizes	 = sizeof(int) * 8;

	for (int i = 1; i <= uint_bit_sizes; value >>= 1, i++)
	{
		if (value & 1)
			reture_value |= 1 << (uint_bit_sizes - i);
	}
	return reture_value;
}

/*
** @param [in] bit_index, the bit to be dealt with ,begin from 0
*/
void set_bit(char bit_array[], unsigned int bit_index)
{
	/* x is the char index to be operated in the bit_array,
	** k is the index to be setted in the char
	*/
	int x = 0, k = 0;

	x = bit_index / 8;
	k = bit_index % 8;

	bit_array[x] |= (1 << k);
	/**actually we can this in one stmt: bit_array[bit_index / 8] != (1 << (bit_index % 8)) **/
}

void clear_bit(char bit_array[], unsigned int bit_index)
{
	/* x is the char index to be operated in the bit_array,
	** k is the index to be setted in the char
	*/
	int x = 0, k = 0;

	x = bit_index / 8;
	k = bit_index % 8;

	bit_array[x] &= ~(1 << k);

	/**actually we can this in one stmt: bit_array[bit_index / 8] &= ~(1 << (bit_index % 8)) **/
}

void assign_bit(char bit_array[], unsigned int bit_index, int value)
{
	if (value)
		set_bit(bit_array, bit_index);
	else
		clear_bit(bit_array, bit_index);
}

int test_bit(char bit_array[], unsigned int bit_index)
{
	/* x is the char index to be operated in the bit_array,
	** k is the index to be setted in the char
	*/
	int x = 0, k = 0;

	x = bit_index / 8;
	k = bit_index % 8;

	/* example is like this: bit_array[x] & 000k000.
	** so the result now determine by the indexed bit.  
	*/
	return bit_array[x] & (1 << k);
	/**actually we can this in one stmt: bit_array[bit_index / 8] &(1 << (bit_index % 8)) **/
}