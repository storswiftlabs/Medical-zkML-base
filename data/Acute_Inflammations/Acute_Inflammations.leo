program dt.aleo {
	struct Inputs {
		p1: u32,
		p2: u32,
		p3: u32,
		p4: u32,
		p5: u32,
	}
	// Code auto generated from DecisionTreeClassifier using dt_to_leo_code.py 
	transition main(inputs: Inputs) -> public u32 {
		if (inputs.p3 < 1u32) {
			if (inputs.p4 < 1u32) {
				return 0u32;
			} else {
				return 1u32;
			}
		} else {
			if (inputs.p1 < 38u32) {
				return 0u32;
			} else {
				if (inputs.p5 < 1u32) {
					return 2u32;
				} else {
					if (inputs.p4 < 1u32) {
						return 2u32;
					} else {
						return 3u32;
					}
				}
			}
		}
	}
}