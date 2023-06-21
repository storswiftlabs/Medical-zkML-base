program dt.aleo {
	// Code auto generated from DecisionTreeClassifier using dt_to_leo_code.py 
	transition main(p1: u32, p2: u32, p3: u32, p4: u32, p5: u32, p6: u32, p7: u32, p8: u32, p9: u32, p10: u32) -> public u32 {
		if (p4 < 1u32) {
			if (p5 < 1u32) {
				return 1u32;
			} else {
				return 0u32;
			}
		} else {
			if (p6 < 1u32) {
				if (p1 < 1u32) {
					return 2u32;
				} else {
					return 0u32;
				}
			} else {
				if (p7 < 1u32) {
					return 3u32;
				} else {
					return 2u32;
				}
			}
		}
	}
}