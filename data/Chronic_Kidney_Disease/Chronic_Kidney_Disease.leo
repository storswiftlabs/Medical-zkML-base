program dt.aleo {
	struct Inputs {
		p1: u32,
		p2: u32,
		p3: u32,
		p4: u32,
		p5: u32,
		p6: u32,
		p7: u32,
		p8: u32,
		p9: u32,
		p10: u32,
		p11: u32,
		p12: u32,
		p13: u32,
		p14: u32,
		p15: u32,
		p16: u32,
		p17: u32,
		p18: u32,
		p19: u32,
		p20: u32,
		p21: u32,
		p22: u32,
		p23: u32,
		p24: u32,
	}
	// Code auto generated from DecisionTreeClassifier using dt_to_leo_code.py 
	transition main(inputs: Inputs) -> public u32 {
		if (inputs.p17 < 42u32) {
			if (inputs.p13 < 40u32) {
				return 0u32;
			} else {
				if (inputs.p16 <= 83500u32) {
					if (inputs.p2 <= 1050u32) {
						return 0u32;
					} else {
						return 1u32;
					}
				} else {
					if (inputs.p17 < 30u32) {
						return 0u32;
					} else {
						if (inputs.p15 <= 350u32) {
							return 1u32;
						} else {
							return 0u32;
						}
					}
				}
			}
		} else {
			if (inputs.p15 <= 340u32) {
				return 0u32;
			} else {
				return 1u32;
			}
		}
	}
}