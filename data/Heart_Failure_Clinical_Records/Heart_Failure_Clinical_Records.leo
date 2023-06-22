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
		if (inputs.p12 < 68u32) {
			if (inputs.p8 < 1u32) {
				if (inputs.p7 <= 191000u32) {
					return 1u32;
				} else {
					return 0u32;
				}
			} else {
				if (inputs.p5 < 73u32) {
					if (inputs.p3 < 110u32) {
						if (inputs.p9 < 136u32) {
							return 1u32;
						} else {
							if (inputs.p9 < 139u32) {
								return 0u32;
							} else {
								if (inputs.p6 < 1u32) {
									return 0u32;
								} else {
									return 1u32;
								}
							}
						}
					} else {
						if (inputs.p3 < 1756u32) {
							if (inputs.p3 <= 160u32) {
								if (inputs.p3 <= 158u32) {
									if (inputs.p5 <= 45u32) {
										return 1u32;
									} else {
										if (inputs.p7 < 240680u32) {
											return 0u32;
										} else {
											return 1u32;
										}
									}
								} else {
									return 0u32;
								}
							} else {
								return 1u32;
							}
						} else {
							if (inputs.p7 < 284180u32) {
								return 1u32;
							} else {
								return 0u32;
							}
						}
					}
				} else {
					return 0u32;
				}
			}
		} else {
			if (inputs.p5 < 33u32) {
				if (inputs.p8 < 2u32) {
					if (inputs.p12 < 79u32) {
						return 1u32;
					} else {
						if (inputs.p8 < 2u32) {
							if (inputs.p1 < 59u32) {
								return 0u32;
							} else {
								if (inputs.p12 <= 169u32) {
									return 1u32;
								} else {
									return 0u32;
								}
							}
						} else {
							if (inputs.p1 <= 56u32) {
								return 1u32;
							} else {
								if (inputs.p11 < 1u32) {
									return 0u32;
								} else {
									if (inputs.p7 <= 204000u32) {
										return 0u32;
									} else {
										if (inputs.p12 <= 191u32) {
											return 1u32;
										} else {
											return 0u32;
										}
									}
								}
							}
						}
					}
				} else {
					if (inputs.p3 <= 65u32) {
						return 0u32;
					} else {
						if (inputs.p12 < 110u32) {
							if (inputs.p10 < 1u32) {
								return 1u32;
							} else {
								return 0u32;
							}
						} else {
							return 1u32;
						}
					}
				}
			} else {
				if (inputs.p8 < 3u32) {
					if (inputs.p8 < 1u32) {
						return 1u32;
					} else {
						if (inputs.p1 < 80u32) {
							if (inputs.p7 <= 90000u32) {
								if (inputs.p12 <= 186u32) {
									return 1u32;
								} else {
									return 0u32;
								}
							} else {
								if (inputs.p9 <= 144u32) {
									if (inputs.p7 <= 344000u32) {
										return 0u32;
									} else {
										if (inputs.p7 <= 354500u32) {
											return 1u32;
										} else {
											return 0u32;
										}
									}
								} else {
									if (inputs.p8 < 2u32) {
										return 0u32;
									} else {
										return 1u32;
									}
								}
							}
						} else {
							if (inputs.p9 <= 135u32) {
								return 1u32;
							} else {
								return 0u32;
							}
						}
					}
				} else {
					if (inputs.p6 < 1u32) {
						if (inputs.p8 < 4u32) {
							return 0u32;
						} else {
							if (inputs.p12 < 102u32) {
								return 1u32;
							} else {
								return 0u32;
							}
						}
					} else {
						return 1u32;
					}
				}
			}
		}
	}
}