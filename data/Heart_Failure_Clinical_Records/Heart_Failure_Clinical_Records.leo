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
	}
	// Code auto generated from DecisionTreeClassifier using dt_to_leo_code.py 
	transition main(inputs: Inputs) -> public u32 {
		if (inputs.p12 <= 69u32) {
			if (inputs.p5 < 73u32) {
				if (inputs.p3 < 81u32) {
					if (inputs.p9 < 135u32) {
						return 1u32;
					} else {
						return 0u32;
					}
				} else {
					if (inputs.p4 < 1u32) {
						return 1u32;
					} else {
						if (inputs.p12 <= 34u32) {
							if (inputs.p5 < 33u32) {
								if (inputs.p7 <= 227500u32) {
									return 1u32;
								} else {
									return 0u32;
								}
							} else {
								if (inputs.p1 <= 71u32) {
									return 1u32;
								} else {
									if (inputs.p3 < 138u32) {
										return 0u32;
									} else {
										return 1u32;
									}
								}
							}
						} else {
							return 1u32;
						}
					}
				}
			} else {
				return 0u32;
			}
		} else {
			if (inputs.p8 < 2u32) {
				if (inputs.p5 < 28u32) {
					if (inputs.p12 < 79u32) {
						return 1u32;
					} else {
						if (inputs.p3 < 1458u32) {
							if (inputs.p11 < 1u32) {
								return 0u32;
							} else {
								if (inputs.p7 <= 204000u32) {
									return 0u32;
								} else {
									if (inputs.p7 <= 241500u32) {
										return 1u32;
									} else {
										if (inputs.p8 < 2u32) {
											return 0u32;
										} else {
											return 1u32;
										}
									}
								}
							}
						} else {
							return 1u32;
						}
					}
				} else {
					if (inputs.p1 <= 79u32) {
						if (inputs.p8 < 2u32) {
							if (inputs.p8 < 2u32) {
								return 0u32;
							} else {
								if (inputs.p5 <= 55u32) {
									return 0u32;
								} else {
									if (inputs.p1 < 73u32) {
										return 1u32;
									} else {
										return 0u32;
									}
								}
							}
						} else {
							if (inputs.p5 < 33u32) {
								return 1u32;
							} else {
								return 0u32;
							}
						}
					} else {
						if (inputs.p9 < 136u32) {
							if (inputs.p3 < 858u32) {
								return 1u32;
							} else {
								return 0u32;
							}
						} else {
							return 0u32;
						}
					}
				}
			} else {
				if (inputs.p8 < 3u32) {
					if (inputs.p8 < 2u32) {
						if (inputs.p7 <= 316000u32) {
							if (inputs.p7 < 253680u32) {
								if (inputs.p12 <= 150u32) {
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
					} else {
						if (inputs.p7 <= 288000u32) {
							return 1u32;
						} else {
							if (inputs.p9 <= 139u32) {
								return 0u32;
							} else {
								return 1u32;
							}
						}
					}
				} else {
					if (inputs.p8 < 8u32) {
						return 0u32;
					} else {
						return 1u32;
					}
				}
			}
		}
	}
}