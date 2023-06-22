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
	}
	// Code auto generated from DecisionTreeClassifier using dt_to_leo_code.py 
	transition main(inputs: Inputs) -> public u32 {
		if (inputs.p19 < -6u32) {
			if (inputs.p1 < 191u32) {
				if (inputs.p16 < 26u32) {
					return 0u32;
				} else {
					return 1u32;
				}
			} else {
				return 0u32;
			}
		} else {
			if (inputs.p20 < 1u32) {
				if (inputs.p18 < 1u32) {
					return 0u32;
				} else {
					if (inputs.p15 < 1u32) {
						return 0u32;
					} else {
						return 1u32;
					}
				}
			} else {
				if (inputs.p2 < 591u32) {
					if (inputs.p8 < 1u32) {
						if (inputs.p1 < 118u32) {
							if (inputs.p13 < 1u32) {
								return 0u32;
							} else {
								return 1u32;
							}
						} else {
							if (inputs.p4 < 1u32) {
								return 1u32;
							} else {
								return 0u32;
							}
						}
					} else {
						if (inputs.p17 < 1u32) {
							if (inputs.p21 < 3u32) {
								return 1u32;
							} else {
								return 0u32;
							}
						} else {
							return 1u32;
						}
					}
				} else {
					return 0u32;
				}
			}
		}
	}
}