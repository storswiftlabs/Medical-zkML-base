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
	}
	// Code auto generated from DecisionTreeClassifier using dt_to_leo_code.py 
	transition main(inputs: Inputs) -> public u32 {
		if (inputs.p1 < 15u32) {
			if (inputs.p12 < 15u32) {
				return 0u32;
			} else {
				if (inputs.p5 < 25u32) {
					if (inputs.p13 < 15u32) {
						return 1u32;
					} else {
						return 0u32;
					}
				} else {
					if (inputs.p6 < 15u32) {
						return 0u32;
					} else {
						if (inputs.p2 < 15u32) {
							return 0u32;
						} else {
							if (inputs.p4 < 15u32) {
								if (inputs.p2 < 25u32) {
									if (inputs.p10 < 15u32) {
										return 1u32;
									} else {
										return 0u32;
									}
								} else {
									return 1u32;
								}
							} else {
								return 1u32;
							}
						}
					}
				}
			}
		} else {
			if (inputs.p6 < 15u32) {
				return 0u32;
			} else {
				if (inputs.p9 < 15u32) {
					return 1u32;
				} else {
					if (inputs.p1 < 35u32) {
						return 1u32;
					} else {
						if (inputs.p1 < 45u32) {
							if (inputs.p15 < 15u32) {
								return 1u32;
							} else {
								return 0u32;
							}
						} else {
							if (inputs.p1 < 165u32) {
								if (inputs.p2 < 25u32) {
									if (inputs.p8 < 15u32) {
										return 1u32;
									} else {
										if (inputs.p3 < 15u32) {
											if (inputs.p7 < 15u32) {
												return 1u32;
											} else {
												if (inputs.p1 < 135u32) {
													if (inputs.p16 < 15u32) {
														return 1u32;
													} else {
														if (inputs.p4 < 25u32) {
															if (inputs.p5 <= 20u32) {
																if (inputs.p14 < 15u32) {
																	return 0u32;
																} else {
																	return 1u32;
																}
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
										} else {
											return 1u32;
										}
									}
								} else {
									return 1u32;
								}
							} else {
								if (inputs.p16 < 15u32) {
									return 0u32;
								} else {
									if (inputs.p14 < 15u32) {
										return 1u32;
									} else {
										if (inputs.p17 < 15u32) {
											if (inputs.p3 < 15u32) {
												return 1u32;
											} else {
												return 0u32;
											}
										} else {
											return 0u32;
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}
}